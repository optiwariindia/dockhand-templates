# VS Code Tunnel (Om Prakash Tiwari) Dockhand Template

**Category:** Development  
**Default Image:** `optiwariindia/vscode-tunnel:latest`

---

## 📖 Description
VS Code Tunnel server container for remote, secure web-based IDE access.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `8000:8000`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `TUNNEL_NAME` | Unique identifier name for VS Code Tunnel | `dockhand-vscode` |
| `DATA_PATH` | Host path for user settings and extensions | `./data/vscode-tunnel` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `vscode-tunnel.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `vscode-tunnel` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.vscode-tunnel.rule=Host(`vscode-tunnel.example.com`)"
  - "traefik.http.routers.vscode-tunnel.entrypoints=websecure"
  - "traefik.http.routers.vscode-tunnel.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
vscode-tunnel.example.com {
    reverse_proxy vscode-tunnel:8000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop vscode-tunnel
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf vscode-tunnel-backup-$(date +%F).tar.gz ./data/vscode-tunnel
   ```
3. Restart the container:
   ```bash
   docker start vscode-tunnel
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop vscode-tunnel && docker rm vscode-tunnel
   ```
2. Extract backup archive to `./data/vscode-tunnel`.
3. Redeploy the stack via Dockhand.

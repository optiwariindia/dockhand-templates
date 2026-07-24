# Vaultwarden Dockhand Template

**Category:** Utilities  
**Default Image:** `vaultwarden/server:latest`

---

## 📖 Description
Unofficial Bitwarden compatible server written in Rust, light on memory.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `8080:80`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `WEBSOCKET_ENABLED` | Enable WebSocket notifications | `true` |
| `DATA_PATH` | Host directory for vault database & attachments | `./data/vaultwarden` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `vaultwarden.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `vaultwarden` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.vaultwarden.rule=Host(`vaultwarden.example.com`)"
  - "traefik.http.routers.vaultwarden.entrypoints=websecure"
  - "traefik.http.routers.vaultwarden.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
vaultwarden.example.com {
    reverse_proxy vaultwarden:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop vaultwarden
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf vaultwarden-backup-$(date +%F).tar.gz ./data/vaultwarden
   ```
3. Restart the container:
   ```bash
   docker start vaultwarden
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop vaultwarden && docker rm vaultwarden
   ```
2. Extract backup archive to `./data/vaultwarden`.
3. Redeploy the stack via Dockhand.

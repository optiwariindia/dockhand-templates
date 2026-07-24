# Tailscale Dockhand Template

**Category:** Networking  
**Default Image:** `tailscale/tailscale:latest`

---

## 📖 Description
Zero-config VPN that creates a secure mesh network among all your devices.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* None (Uses internal network or volume mount)

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `TS_AUTHKEY` | Tailscale reusable or ephemeral authentication key | `` |
| `TS_EXTRA_ARGS` | Additional flags (e.g. --advertise-routes=192.168.1.0/24) | `--advertise-exit-node` |
| `TS_STATE_DIR` | Host directory for persistent state | `./data/tailscale` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `tailscale.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `tailscale` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.tailscale.rule=Host(`tailscale.example.com`)"
  - "traefik.http.routers.tailscale.entrypoints=websecure"
  - "traefik.http.routers.tailscale.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
tailscale.example.com {
    reverse_proxy tailscale:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop tailscale
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf tailscale-backup-$(date +%F).tar.gz ./data/tailscale
   ```
3. Restart the container:
   ```bash
   docker start tailscale
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop tailscale && docker rm tailscale
   ```
2. Extract backup archive to `./data/tailscale`.
3. Redeploy the stack via Dockhand.

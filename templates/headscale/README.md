# Headscale Dockhand Template

**Category:** Networking  
**Default Image:** `headscale/headscale:latest`

---

## 📖 Description
Open-source, self-hosted implementation of the Tailscale control server.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `8080:8080`
* `9090:9090`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `CONFIG_PATH` | Host directory for config.yaml | `./config/headscale` |
| `DATA_PATH` | Host path for Headscale SQLite/state data | `./data/headscale` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `headscale.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `headscale` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.headscale.rule=Host(`headscale.example.com`)"
  - "traefik.http.routers.headscale.entrypoints=websecure"
  - "traefik.http.routers.headscale.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
headscale.example.com {
    reverse_proxy headscale:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop headscale
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf headscale-backup-$(date +%F).tar.gz ./data/headscale
   ```
3. Restart the container:
   ```bash
   docker start headscale
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop headscale && docker rm headscale
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf headscale-backup-YYYY-MM-DD.tar.gz -C ./data/headscale
   ```
3. Redeploy the stack via Dockhand.

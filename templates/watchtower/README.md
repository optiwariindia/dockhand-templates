# Watchtower Dockhand Template

**Category:** Utilities  
**Default Image:** `containrrr/watchtower:latest`

---

## 📖 Description
Automated Docker container base image updater.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* None (Uses host network or mesh overlay)

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `WATCHTOWER_CLEANUP` | Remove old images after updating | `true` |
| `WATCHTOWER_SCHEDULE` | Cron expression for update checks | `0 0 4 * * *` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `watchtower.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `watchtower` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.watchtower.rule=Host(`watchtower.example.com`)"
  - "traefik.http.routers.watchtower.entrypoints=websecure"
  - "traefik.http.routers.watchtower.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
watchtower.example.com {
    reverse_proxy watchtower:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop watchtower
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf watchtower-backup-$(date +%F).tar.gz ./data/watchtower
   ```
3. Restart the container:
   ```bash
   docker start watchtower
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop watchtower && docker rm watchtower
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf watchtower-backup-YYYY-MM-DD.tar.gz -C ./data/watchtower
   ```
3. Redeploy the stack via Dockhand.

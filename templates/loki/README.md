# Loki Dockhand Template

**Category:** Monitoring  
**Default Image:** `grafana/loki:latest`

---

## 📖 Description
Like Prometheus, but for logs. High performance log aggregation system.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `3100:3100`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host path for log index and chunk storage | `./data/loki` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `loki.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `loki` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.loki.rule=Host(`loki.example.com`)"
  - "traefik.http.routers.loki.entrypoints=websecure"
  - "traefik.http.routers.loki.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
loki.example.com {
    reverse_proxy loki:3100
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop loki
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf loki-backup-$(date +%F).tar.gz ./data/loki
   ```
3. Restart the container:
   ```bash
   docker start loki
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop loki && docker rm loki
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf loki-backup-YYYY-MM-DD.tar.gz -C ./data/loki
   ```
3. Redeploy the stack via Dockhand.

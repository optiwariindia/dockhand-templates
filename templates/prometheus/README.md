# Prometheus Dockhand Template

**Category:** Monitoring  
**Default Image:** `prom/prometheus:latest`

---

## 📖 Description
Open-source monitoring system and time-series database.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `9090:9090`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host path for TSDB metric persistence | `./data/prometheus` |
| `CONFIG_PATH` | Host path for prometheus.yml config file | `./config/prometheus` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `prometheus.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `prometheus` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.prometheus.rule=Host(`prometheus.example.com`)"
  - "traefik.http.routers.prometheus.entrypoints=websecure"
  - "traefik.http.routers.prometheus.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
prometheus.example.com {
    reverse_proxy prometheus:9090
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop prometheus
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf prometheus-backup-$(date +%F).tar.gz ./data/prometheus
   ```
3. Restart the container:
   ```bash
   docker start prometheus
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop prometheus && docker rm prometheus
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf prometheus-backup-YYYY-MM-DD.tar.gz -C ./data/prometheus
   ```
3. Redeploy the stack via Dockhand.

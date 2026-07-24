# BizBandhan Trace RUM (Om Prakash Tiwari) Dockhand Template

**Category:** Monitoring  
**Default Image:** `optiwariindia/bizbandhan-trace:latest`

---

## 📖 Description
Lightweight, OpenTelemetry-native Real-User Monitoring (RUM) telemetry ingestion service.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `4318:4318`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `PORT` | OTLP/HTTP ingestion port | `4318` |
| `DATA_PATH` | Host path for local traces storage | `./data/bizbandhan-trace` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `bizbandhan-trace.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `bizbandhan-trace` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.bizbandhan-trace.rule=Host(`bizbandhan-trace.example.com`)"
  - "traefik.http.routers.bizbandhan-trace.entrypoints=websecure"
  - "traefik.http.routers.bizbandhan-trace.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
bizbandhan-trace.example.com {
    reverse_proxy bizbandhan-trace:4318
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop bizbandhan-trace
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf bizbandhan-trace-backup-$(date +%F).tar.gz ./data/bizbandhan-trace
   ```
3. Restart the container:
   ```bash
   docker start bizbandhan-trace
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop bizbandhan-trace && docker rm bizbandhan-trace
   ```
2. Extract backup archive to `./data/bizbandhan-trace`.
3. Redeploy the stack via Dockhand.

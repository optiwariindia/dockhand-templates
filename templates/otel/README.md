# OpenTelemetry Collector (Om Prakash Tiwari) Dockhand Template

**Category:** Monitoring  
**Default Image:** `optiwariindia/otel:latest`

---

## 📖 Description
OpenTelemetry Collector container for metrics, logs, and traces pipeline.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `4317:4317`
* `4318:4318`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `CONFIG_PATH` | Host path for otel-collector-config.yaml | `./config/otel` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `otel.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `otel` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.otel.rule=Host(`otel.example.com`)"
  - "traefik.http.routers.otel.entrypoints=websecure"
  - "traefik.http.routers.otel.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
otel.example.com {
    reverse_proxy otel:4317
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop otel
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf otel-backup-$(date +%F).tar.gz ./data/otel
   ```
3. Restart the container:
   ```bash
   docker start otel
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop otel && docker rm otel
   ```
2. Extract backup archive to `./data/otel`.
3. Redeploy the stack via Dockhand.

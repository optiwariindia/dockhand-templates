# Grafana Dockhand Template

**Category:** Monitoring  
**Default Image:** `grafana/grafana:latest`

---

## 📖 Description
The open and composable observability and data visualization platform.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `3000:3000`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `GF_SECURITY_ADMIN_USER` | Grafana administrator username | `admin` |
| `GF_SECURITY_ADMIN_PASSWORD` | Grafana administrator password | `changeme123` |
| `DATA_PATH` | Host path for storing Grafana dashboards and DB | `./data/grafana` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `grafana.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `grafana` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.grafana.rule=Host(`grafana.example.com`)"
  - "traefik.http.routers.grafana.entrypoints=websecure"
  - "traefik.http.routers.grafana.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
grafana.example.com {
    reverse_proxy grafana:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop grafana
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf grafana-backup-$(date +%F).tar.gz ./data/grafana
   ```
3. Restart the container:
   ```bash
   docker start grafana
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop grafana && docker rm grafana
   ```
2. Extract backup archive to `./data/grafana`.
3. Redeploy the stack via Dockhand.

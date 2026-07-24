# Stirling PDF Dockhand Template

**Category:** Utilities  
**Default Image:** `frooodle/s-pdf:latest`

---

## 📖 Description
Robust, locally hosted web application that allows you to perform operations on PDF files.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `8080:8080`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DOCKER_ENABLE_SECURITY` | Enable user login and security module | `false` |
| `DATA_PATH` | Host directory for OCR training data and custom configs | `./data/stirling-pdf` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `stirling-pdf.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `stirling-pdf` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.stirling-pdf.rule=Host(`stirling-pdf.example.com`)"
  - "traefik.http.routers.stirling-pdf.entrypoints=websecure"
  - "traefik.http.routers.stirling-pdf.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
stirling-pdf.example.com {
    reverse_proxy stirling-pdf:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop stirling-pdf
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf stirling-pdf-backup-$(date +%F).tar.gz ./data/stirling-pdf
   ```
3. Restart the container:
   ```bash
   docker start stirling-pdf
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop stirling-pdf && docker rm stirling-pdf
   ```
2. Extract backup archive to `./data/stirling-pdf`.
3. Redeploy the stack via Dockhand.

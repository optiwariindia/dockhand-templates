# PDF Generator (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/pdf:latest`

---

## 📖 Description
HTML-to-PDF rendering and document compilation microservice.

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
| `PORT` | Server listening port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `pdf.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `pdf` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.pdf.rule=Host(`pdf.example.com`)"
  - "traefik.http.routers.pdf.entrypoints=websecure"
  - "traefik.http.routers.pdf.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
pdf.example.com {
    reverse_proxy pdf:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop pdf
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf pdf-backup-$(date +%F).tar.gz ./data/pdf
   ```
3. Restart the container:
   ```bash
   docker start pdf
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop pdf && docker rm pdf
   ```
2. Extract backup archive to `./data/pdf`.
3. Redeploy the stack via Dockhand.

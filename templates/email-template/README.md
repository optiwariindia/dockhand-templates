# Email Template Service (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/email-template:latest`

---

## 📖 Description
HTML Email Template rendering and live preview server.

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
| `TEMPLATE_DIR` | Host path for custom HTML templates | `./data/email-templates` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `email-template.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `email-template` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.email-template.rule=Host(`email-template.example.com`)"
  - "traefik.http.routers.email-template.entrypoints=websecure"
  - "traefik.http.routers.email-template.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
email-template.example.com {
    reverse_proxy email-template:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop email-template
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf email-template-backup-$(date +%F).tar.gz ./data/email-template
   ```
3. Restart the container:
   ```bash
   docker start email-template
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop email-template && docker rm email-template
   ```
2. Extract backup archive to `./data/email-template`.
3. Redeploy the stack via Dockhand.

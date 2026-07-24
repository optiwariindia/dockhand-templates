# Express Twig Mailer (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/express-twig-mailer:latest`

---

## 📖 Description
Express.js & Twig email dispatch microservice with SMTP support.

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
| `SMTP_HOST` | Outbound SMTP server host | `smtp.example.com` |
| `SMTP_PORT` | Outbound SMTP server port | `587` |
| `SMTP_USER` | SMTP login username | `user@example.com` |
| `SMTP_PASS` | SMTP login password | `smtppass123` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `express-twig-mailer.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `express-twig-mailer` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.express-twig-mailer.rule=Host(`express-twig-mailer.example.com`)"
  - "traefik.http.routers.express-twig-mailer.entrypoints=websecure"
  - "traefik.http.routers.express-twig-mailer.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
express-twig-mailer.example.com {
    reverse_proxy express-twig-mailer:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop express-twig-mailer
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf express-twig-mailer-backup-$(date +%F).tar.gz ./data/express-twig-mailer
   ```
3. Restart the container:
   ```bash
   docker start express-twig-mailer
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop express-twig-mailer && docker rm express-twig-mailer
   ```
2. Extract backup archive to `./data/express-twig-mailer`.
3. Redeploy the stack via Dockhand.

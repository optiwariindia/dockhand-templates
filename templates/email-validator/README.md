# Email Validator API (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/email-validator:latest`

---

## 📖 Description
Email syntax, MX record, and mailbox deliverability checking API.

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
1. Forward host domain (e.g. `email-validator.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `email-validator` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.email-validator.rule=Host(`email-validator.example.com`)"
  - "traefik.http.routers.email-validator.entrypoints=websecure"
  - "traefik.http.routers.email-validator.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
email-validator.example.com {
    reverse_proxy email-validator:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop email-validator
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf email-validator-backup-$(date +%F).tar.gz ./data/email-validator
   ```
3. Restart the container:
   ```bash
   docker start email-validator
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop email-validator && docker rm email-validator
   ```
2. Extract backup archive to `./data/email-validator`.
3. Redeploy the stack via Dockhand.

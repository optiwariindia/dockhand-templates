# CAPTCHA Service (Om Prakash Tiwari) Dockhand Template

**Category:** Security  
**Default Image:** `optiwariindia/captcha:latest`

---

## 📖 Description
CAPTCHA challenge image generation and verification API.

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
| `SECRET_KEY` | Encryption key for signing captcha tokens | `captchasecret123` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `captcha.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `captcha` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.captcha.rule=Host(`captcha.example.com`)"
  - "traefik.http.routers.captcha.entrypoints=websecure"
  - "traefik.http.routers.captcha.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
captcha.example.com {
    reverse_proxy captcha:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop captcha
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf captcha-backup-$(date +%F).tar.gz ./data/captcha
   ```
3. Restart the container:
   ```bash
   docker start captcha
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop captcha && docker rm captcha
   ```
2. Extract backup archive to `./data/captcha`.
3. Redeploy the stack via Dockhand.

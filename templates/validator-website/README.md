# Website Validator (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/validator-website:latest`

---

## 📖 Description
Website availability, SSL validity, and status checking microservice.

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
| `PORT` | Server port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `validator-website.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `validator-website` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.validator-website.rule=Host(`validator-website.example.com`)"
  - "traefik.http.routers.validator-website.entrypoints=websecure"
  - "traefik.http.routers.validator-website.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
validator-website.example.com {
    reverse_proxy validator-website:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop validator-website
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf validator-website-backup-$(date +%F).tar.gz ./data/validator-website
   ```
3. Restart the container:
   ```bash
   docker start validator-website
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop validator-website && docker rm validator-website
   ```
2. Extract backup archive to `./data/validator-website`.
3. Redeploy the stack via Dockhand.

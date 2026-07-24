# Validator Email Service (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/validator-email:latest`

---

## 📖 Description
High-throughput email validation and format verification microservice.

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
1. Forward host domain (e.g. `validator-email.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `validator-email` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.validator-email.rule=Host(`validator-email.example.com`)"
  - "traefik.http.routers.validator-email.entrypoints=websecure"
  - "traefik.http.routers.validator-email.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
validator-email.example.com {
    reverse_proxy validator-email:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop validator-email
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf validator-email-backup-$(date +%F).tar.gz ./data/validator-email
   ```
3. Restart the container:
   ```bash
   docker start validator-email
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop validator-email && docker rm validator-email
   ```
2. Extract backup archive to `./data/validator-email`.
3. Redeploy the stack via Dockhand.

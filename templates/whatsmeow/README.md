# Whatsmeow Listener (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/whatsmeow:latest`

---

## 📖 Description
Lightweight listener and API service for WhatsApp events and webhooks.

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
| `SESSION_PATH` | Host directory for persistent WhatsApp SQLite session DB | `./data/whatsmeow` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `whatsmeow.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `whatsmeow` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.whatsmeow.rule=Host(`whatsmeow.example.com`)"
  - "traefik.http.routers.whatsmeow.entrypoints=websecure"
  - "traefik.http.routers.whatsmeow.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
whatsmeow.example.com {
    reverse_proxy whatsmeow:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop whatsmeow
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf whatsmeow-backup-$(date +%F).tar.gz ./data/whatsmeow
   ```
3. Restart the container:
   ```bash
   docker start whatsmeow
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop whatsmeow && docker rm whatsmeow
   ```
2. Extract backup archive to `./data/whatsmeow`.
3. Redeploy the stack via Dockhand.

# Location IP API (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/location-ip:latest`

---

## 📖 Description
API microservice providing country code and IP Address of host using Whois lookup.

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
| `PORT` | Internal server port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `location-ip.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `location-ip` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.location-ip.rule=Host(`location-ip.example.com`)"
  - "traefik.http.routers.location-ip.entrypoints=websecure"
  - "traefik.http.routers.location-ip.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
location-ip.example.com {
    reverse_proxy location-ip:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop location-ip
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf location-ip-backup-$(date +%F).tar.gz ./data/location-ip
   ```
3. Restart the container:
   ```bash
   docker start location-ip
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop location-ip && docker rm location-ip
   ```
2. Extract backup archive to `./data/location-ip`.
3. Redeploy the stack via Dockhand.

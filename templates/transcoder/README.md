# Transcoder API (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/transcoder:latest`

---

## 📖 Description
High-speed video and audio media transcoding microservice.

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
| `DATA_PATH` | Host directory for incoming and output media files | `./data/transcoder` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `transcoder.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `transcoder` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.transcoder.rule=Host(`transcoder.example.com`)"
  - "traefik.http.routers.transcoder.entrypoints=websecure"
  - "traefik.http.routers.transcoder.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
transcoder.example.com {
    reverse_proxy transcoder:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop transcoder
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf transcoder-backup-$(date +%F).tar.gz ./data/transcoder
   ```
3. Restart the container:
   ```bash
   docker start transcoder
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop transcoder && docker rm transcoder
   ```
2. Extract backup archive to `./data/transcoder`.
3. Redeploy the stack via Dockhand.

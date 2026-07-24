# LiveReload Server (Om Prakash Tiwari) Dockhand Template

**Category:** Development  
**Default Image:** `optiwariindia/livereload:latest`

---

## 📖 Description
LiveReload server for automatically reloading browsers on file changes in Docker.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `35729:35729`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `WATCH_DIR` | Host path containing files to watch for auto-reload | `./data/livereload` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `livereload.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `livereload` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.livereload.rule=Host(`livereload.example.com`)"
  - "traefik.http.routers.livereload.entrypoints=websecure"
  - "traefik.http.routers.livereload.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
livereload.example.com {
    reverse_proxy livereload:35729
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop livereload
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf livereload-backup-$(date +%F).tar.gz ./data/livereload
   ```
3. Restart the container:
   ```bash
   docker start livereload
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop livereload && docker rm livereload
   ```
2. Extract backup archive to `./data/livereload`.
3. Redeploy the stack via Dockhand.

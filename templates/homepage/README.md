# Homepage Dockhand Template

**Category:** Utilities  
**Default Image:** `ghcr.io/gethomepage/homepage:latest`

---

## 📖 Description
A modern, secure, highly customizable application dashboard with integrations.

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
| `CONFIG_PATH` | Host directory for settings.yaml, services.yaml, bookmarks.yaml | `./config/homepage` |
| `PUID` | Process User ID | `1000` |
| `PGID` | Process Group ID | `1000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `homepage.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `homepage` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.homepage.rule=Host(`homepage.example.com`)"
  - "traefik.http.routers.homepage.entrypoints=websecure"
  - "traefik.http.routers.homepage.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
homepage.example.com {
    reverse_proxy homepage:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop homepage
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf homepage-backup-$(date +%F).tar.gz ./data/homepage
   ```
3. Restart the container:
   ```bash
   docker start homepage
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop homepage && docker rm homepage
   ```
2. Extract backup archive to `./data/homepage`.
3. Redeploy the stack via Dockhand.

# Gulp Runner (Om Prakash Tiwari) Dockhand Template

**Category:** Development  
**Default Image:** `optiwariindia/gulp-runner:latest`

---

## 📖 Description
Automated Gulp task runner environment for building frontend assets.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* None (Uses internal network or volume mount)

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `PROJECT_PATH` | Host directory containing Gulpfile.js and source files | `./data/gulp-project` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `gulp-runner.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `gulp-runner` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.gulp-runner.rule=Host(`gulp-runner.example.com`)"
  - "traefik.http.routers.gulp-runner.entrypoints=websecure"
  - "traefik.http.routers.gulp-runner.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
gulp-runner.example.com {
    reverse_proxy gulp-runner:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop gulp-runner
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf gulp-runner-backup-$(date +%F).tar.gz ./data/gulp-runner
   ```
3. Restart the container:
   ```bash
   docker start gulp-runner
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop gulp-runner && docker rm gulp-runner
   ```
2. Extract backup archive to `./data/gulp-runner`.
3. Redeploy the stack via Dockhand.

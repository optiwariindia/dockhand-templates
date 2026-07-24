# Express Environment (Om Prakash Tiwari) Dockhand Template

**Category:** Development  
**Default Image:** `optiwariindia/express:latest`

---

## 📖 Description
Node.js Express application container environment.

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
| `NODE_ENV` | Node.js environment setting | `production` |
| `PORT` | Internal app HTTP port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `express.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `express` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.express.rule=Host(`express.example.com`)"
  - "traefik.http.routers.express.entrypoints=websecure"
  - "traefik.http.routers.express.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
express.example.com {
    reverse_proxy express:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop express
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf express-backup-$(date +%F).tar.gz ./data/express
   ```
3. Restart the container:
   ```bash
   docker start express
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop express && docker rm express
   ```
2. Extract backup archive to `./data/express`.
3. Redeploy the stack via Dockhand.

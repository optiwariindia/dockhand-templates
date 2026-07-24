# React Application Server (Om Prakash Tiwari) Dockhand Template

**Category:** Development  
**Default Image:** `optiwariindia/react-server:latest`

---

## 📖 Description
React web application web server and static asset host.

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
| `PUBLIC_DIR` | Host directory containing built static files | `./data/react-app` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `react-server.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `react-server` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.react-server.rule=Host(`react-server.example.com`)"
  - "traefik.http.routers.react-server.entrypoints=websecure"
  - "traefik.http.routers.react-server.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
react-server.example.com {
    reverse_proxy react-server:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop react-server
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf react-server-backup-$(date +%F).tar.gz ./data/react-server
   ```
3. Restart the container:
   ```bash
   docker start react-server
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop react-server && docker rm react-server
   ```
2. Extract backup archive to `./data/react-server`.
3. Redeploy the stack via Dockhand.

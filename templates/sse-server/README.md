# SSE Broadcasting Server (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/sse-server:latest`

---

## 📖 Description
Lightweight Server-Sent Events (SSE) broadcasting hub.

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
1. Forward host domain (e.g. `sse-server.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `sse-server` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.sse-server.rule=Host(`sse-server.example.com`)"
  - "traefik.http.routers.sse-server.entrypoints=websecure"
  - "traefik.http.routers.sse-server.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
sse-server.example.com {
    reverse_proxy sse-server:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop sse-server
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf sse-server-backup-$(date +%F).tar.gz ./data/sse-server
   ```
3. Restart the container:
   ```bash
   docker start sse-server
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop sse-server && docker rm sse-server
   ```
2. Extract backup archive to `./data/sse-server`.
3. Redeploy the stack via Dockhand.

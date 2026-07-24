# Pravah Go SSE Server (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/pravah-go:latest`

---

## 📖 Description
High-performance Server-Sent Events (SSE) server in Go to sync applications in real-time.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `8080:8080`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `PORT` | Application listening port | `8080` |
| `REDIS_URL` | Optional Redis connection URL for multi-node pub/sub | `` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `pravah-go.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `pravah-go` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.pravah-go.rule=Host(`pravah-go.example.com`)"
  - "traefik.http.routers.pravah-go.entrypoints=websecure"
  - "traefik.http.routers.pravah-go.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
pravah-go.example.com {
    reverse_proxy pravah-go:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop pravah-go
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf pravah-go-backup-$(date +%F).tar.gz ./data/pravah-go
   ```
3. Restart the container:
   ```bash
   docker start pravah-go
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop pravah-go && docker rm pravah-go
   ```
2. Extract backup archive to `./data/pravah-go`.
3. Redeploy the stack via Dockhand.

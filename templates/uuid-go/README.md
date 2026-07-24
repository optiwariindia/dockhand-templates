# UUID Go Generator (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/uuid-go:latest`

---

## 📖 Description
High-throughput UUID generation microservice built in Go.

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
| `PORT` | Application port | `8080` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `uuid-go.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `uuid-go` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.uuid-go.rule=Host(`uuid-go.example.com`)"
  - "traefik.http.routers.uuid-go.entrypoints=websecure"
  - "traefik.http.routers.uuid-go.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
uuid-go.example.com {
    reverse_proxy uuid-go:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop uuid-go
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf uuid-go-backup-$(date +%F).tar.gz ./data/uuid-go
   ```
3. Restart the container:
   ```bash
   docker start uuid-go
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop uuid-go && docker rm uuid-go
   ```
2. Extract backup archive to `./data/uuid-go`.
3. Redeploy the stack via Dockhand.

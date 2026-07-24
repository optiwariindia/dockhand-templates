# API Gateway (Om Prakash Tiwari) Dockhand Template

**Category:** Reverse Proxy  
**Default Image:** `optiwariindia/gateway:latest`

---

## 📖 Description
Lightweight API Gateway service for routing microservice requests.

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
| `CONFIG_PATH` | Host path for gateway routes configuration | `./config/gateway` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `gateway.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `gateway` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.gateway.rule=Host(`gateway.example.com`)"
  - "traefik.http.routers.gateway.entrypoints=websecure"
  - "traefik.http.routers.gateway.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
gateway.example.com {
    reverse_proxy gateway:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop gateway
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf gateway-backup-$(date +%F).tar.gz ./data/gateway
   ```
3. Restart the container:
   ```bash
   docker start gateway
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop gateway && docker rm gateway
   ```
2. Extract backup archive to `./data/gateway`.
3. Redeploy the stack via Dockhand.

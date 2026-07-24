# Get-PTR Resolver (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/get-ptr:latest`

---

## 📖 Description
Reverse DNS (PTR record) lookup microservice.

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
| `PORT` | Internal HTTP port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `get-ptr.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `get-ptr` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.get-ptr.rule=Host(`get-ptr.example.com`)"
  - "traefik.http.routers.get-ptr.entrypoints=websecure"
  - "traefik.http.routers.get-ptr.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
get-ptr.example.com {
    reverse_proxy get-ptr:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop get-ptr
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf get-ptr-backup-$(date +%F).tar.gz ./data/get-ptr
   ```
3. Restart the container:
   ```bash
   docker start get-ptr
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop get-ptr && docker rm get-ptr
   ```
2. Extract backup archive to `./data/get-ptr`.
3. Redeploy the stack via Dockhand.

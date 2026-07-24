# GetCN Inspector (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/getcn:latest`

---

## 📖 Description
SSL Certificate inspector and Common Name (CN) extraction microservice.

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
| `PORT` | Internal server port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `getcn.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `getcn` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.getcn.rule=Host(`getcn.example.com`)"
  - "traefik.http.routers.getcn.entrypoints=websecure"
  - "traefik.http.routers.getcn.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
getcn.example.com {
    reverse_proxy getcn:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop getcn
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf getcn-backup-$(date +%F).tar.gz ./data/getcn
   ```
3. Restart the container:
   ```bash
   docker start getcn
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop getcn && docker rm getcn
   ```
2. Extract backup archive to `./data/getcn`.
3. Redeploy the stack via Dockhand.

# Excel Microservice (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/excel:latest`

---

## 📖 Description
Excel spreadsheet parsing, data generation, and transformation API.

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
| `PORT` | Server listening port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `excel.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `excel` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.excel.rule=Host(`excel.example.com`)"
  - "traefik.http.routers.excel.entrypoints=websecure"
  - "traefik.http.routers.excel.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
excel.example.com {
    reverse_proxy excel:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop excel
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf excel-backup-$(date +%F).tar.gz ./data/excel
   ```
3. Restart the container:
   ```bash
   docker start excel
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop excel && docker rm excel
   ```
2. Extract backup archive to `./data/excel`.
3. Redeploy the stack via Dockhand.

# ExRate API (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/exrate:latest`

---

## 📖 Description
Exchange rate API with daily caching and multi-currency conversion support.

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
| `CACHE_TTL` | Expiration time for cached exchange rates | `86400` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `exrate.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `exrate` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.exrate.rule=Host(`exrate.example.com`)"
  - "traefik.http.routers.exrate.entrypoints=websecure"
  - "traefik.http.routers.exrate.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
exrate.example.com {
    reverse_proxy exrate:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop exrate
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf exrate-backup-$(date +%F).tar.gz ./data/exrate
   ```
3. Restart the container:
   ```bash
   docker start exrate
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop exrate && docker rm exrate
   ```
2. Extract backup archive to `./data/exrate`.
3. Redeploy the stack via Dockhand.

# Address Options API (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/address-options:latest`

---

## 📖 Description
API server providing complete, structured lists of countries, states, and cities.

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
| `PORT` | Internal application HTTP port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `address-options.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `address-options` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.address-options.rule=Host(`address-options.example.com`)"
  - "traefik.http.routers.address-options.entrypoints=websecure"
  - "traefik.http.routers.address-options.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
address-options.example.com {
    reverse_proxy address-options:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop address-options
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf address-options-backup-$(date +%F).tar.gz ./data/address-options
   ```
3. Restart the container:
   ```bash
   docker start address-options
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop address-options && docker rm address-options
   ```
2. Extract backup archive to `./data/address-options`.
3. Redeploy the stack via Dockhand.

# Dozzle Dockhand Template

**Category:** Utilities  
**Default Image:** `amir20/dozzle:latest`

---

## 📖 Description
Real-time log viewer for Docker containers in your browser.

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
| `DOZZLE_LEVEL` | Dozzle process logging verbosity | `info` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `dozzle.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `dozzle` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.dozzle.rule=Host(`dozzle.example.com`)"
  - "traefik.http.routers.dozzle.entrypoints=websecure"
  - "traefik.http.routers.dozzle.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
dozzle.example.com {
    reverse_proxy dozzle:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop dozzle
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf dozzle-backup-$(date +%F).tar.gz ./data/dozzle
   ```
3. Restart the container:
   ```bash
   docker start dozzle
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop dozzle && docker rm dozzle
   ```
2. Extract backup archive to `./data/dozzle`.
3. Redeploy the stack via Dockhand.

# Traefik Dockhand Template

**Category:** Reverse Proxy  
**Default Image:** `traefik:v3.1`

---

## 📖 Description
Cloud-native edge router and HTTP reverse proxy with auto-discovery.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `80:80`
* `443:443`
* `8080:8080`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host path for dynamic configuration & acme.json | `./data/traefik` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `traefik.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `traefik` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.traefik.rule=Host(`traefik.example.com`)"
  - "traefik.http.routers.traefik.entrypoints=websecure"
  - "traefik.http.routers.traefik.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
traefik.example.com {
    reverse_proxy traefik:80
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop traefik
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf traefik-backup-$(date +%F).tar.gz ./data/traefik
   ```
3. Restart the container:
   ```bash
   docker start traefik
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop traefik && docker rm traefik
   ```
2. Extract backup archive to `./data/traefik`.
3. Redeploy the stack via Dockhand.

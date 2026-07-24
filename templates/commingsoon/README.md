# Coming Soon Server (Om Prakash Tiwari) Dockhand Template

**Category:** Utilities  
**Default Image:** `optiwariindia/commingsoon:latest`

---

## 📖 Description
Lightweight Coming Soon / Maintenance page web server.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `8080:80`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `TITLE` | Main title displayed on coming soon page | `Coming Soon` |
| `SUBTITLE` | Subtitle text description | `We are launching our new application soon!` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `commingsoon.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `commingsoon` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.commingsoon.rule=Host(`commingsoon.example.com`)"
  - "traefik.http.routers.commingsoon.entrypoints=websecure"
  - "traefik.http.routers.commingsoon.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
commingsoon.example.com {
    reverse_proxy commingsoon:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop commingsoon
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf commingsoon-backup-$(date +%F).tar.gz ./data/commingsoon
   ```
3. Restart the container:
   ```bash
   docker start commingsoon
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop commingsoon && docker rm commingsoon
   ```
2. Extract backup archive to `./data/commingsoon`.
3. Redeploy the stack via Dockhand.

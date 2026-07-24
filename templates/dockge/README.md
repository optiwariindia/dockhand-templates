# Dockge Dockhand Template

**Category:** Development  
**Default Image:** `louislam/dockge:1`

---

## 📖 Description
A slick, user-friendly & reactive self-hosted Docker Compose manager.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `5001:5001`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `STACKS_DIR` | Host path where Docker compose stacks are stored | `/opt/stacks` |
| `DATA_PATH` | Host path for Dockge database | `./data/dockge` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `dockge.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `dockge` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.dockge.rule=Host(`dockge.example.com`)"
  - "traefik.http.routers.dockge.entrypoints=websecure"
  - "traefik.http.routers.dockge.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
dockge.example.com {
    reverse_proxy dockge:5001
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop dockge
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf dockge-backup-$(date +%F).tar.gz ./data/dockge
   ```
3. Restart the container:
   ```bash
   docker start dockge
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop dockge && docker rm dockge
   ```
2. Extract backup archive to `./data/dockge`.
3. Redeploy the stack via Dockhand.

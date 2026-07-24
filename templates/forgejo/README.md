# Forgejo Dockhand Template

**Category:** Development  
**Default Image:** `codeberg.org/forgejo/forgejo:9`

---

## 📖 Description
Self-hosted lightweight software development platform driven by the community.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `3000:3000`
* `2222:22`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `USER_UID` | UID for user execution | `1000` |
| `USER_GID` | GID for group execution | `1000` |
| `DATA_PATH` | Host path for repositories & state | `./data/forgejo` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `forgejo.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `forgejo` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.forgejo.rule=Host(`forgejo.example.com`)"
  - "traefik.http.routers.forgejo.entrypoints=websecure"
  - "traefik.http.routers.forgejo.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
forgejo.example.com {
    reverse_proxy forgejo:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop forgejo
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf forgejo-backup-$(date +%F).tar.gz ./data/forgejo
   ```
3. Restart the container:
   ```bash
   docker start forgejo
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop forgejo && docker rm forgejo
   ```
2. Extract backup archive to `./data/forgejo`.
3. Redeploy the stack via Dockhand.

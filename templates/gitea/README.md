# Gitea Dockhand Template

**Category:** Development  
**Default Image:** `gitea/gitea:latest`

---

## 📖 Description
Painless self-hosted Git service written in Go.

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
| `USER_UID` | UID for Gitea process execution | `1000` |
| `USER_GID` | GID for Gitea process execution | `1000` |
| `DATA_PATH` | Host directory for git repositories and user data | `./data/gitea` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `gitea.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `gitea` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.gitea.rule=Host(`gitea.example.com`)"
  - "traefik.http.routers.gitea.entrypoints=websecure"
  - "traefik.http.routers.gitea.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
gitea.example.com {
    reverse_proxy gitea:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop gitea
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf gitea-backup-$(date +%F).tar.gz ./data/gitea
   ```
3. Restart the container:
   ```bash
   docker start gitea
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop gitea && docker rm gitea
   ```
2. Extract backup archive to `./data/gitea`.
3. Redeploy the stack via Dockhand.

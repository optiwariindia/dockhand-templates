# FileBrowser Dockhand Template

**Category:** Utilities  
**Default Image:** `filebrowser/filebrowser:latest`

---

## 📖 Description
Web-based file management interface to upload, edit, preview, and share files.

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
| `DATA_PATH` | Host path for managed storage files | `./data/filebrowser/files` |
| `DATABASE_PATH` | Host path for filebrowser.db SQLite file | `./data/filebrowser/filebrowser.db` |
| `CONFIG_PATH` | Host path for settings.json | `./config/filebrowser/settings.json` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `filebrowser.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `filebrowser` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.filebrowser.rule=Host(`filebrowser.example.com`)"
  - "traefik.http.routers.filebrowser.entrypoints=websecure"
  - "traefik.http.routers.filebrowser.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
filebrowser.example.com {
    reverse_proxy filebrowser:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop filebrowser
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf filebrowser-backup-$(date +%F).tar.gz ./data/filebrowser
   ```
3. Restart the container:
   ```bash
   docker start filebrowser
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop filebrowser && docker rm filebrowser
   ```
2. Extract backup archive to `./data/filebrowser`.
3. Redeploy the stack via Dockhand.

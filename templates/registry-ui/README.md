# Registry UI Dockhand Template

**Category:** Development  
**Default Image:** `joxit/docker-registry-ui:latest`

---

## 📖 Description
User interface for private Docker registries to search and manage container tags.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `8080:80`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `REGISTRY_TITLE` | UI Display Title | `My Private Registry` |
| `REGISTRY_URL` | URL of the target Registry v2 service | `http://registry:5000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `registry-ui.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `registry-ui` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.registry-ui.rule=Host(`registry-ui.example.com`)"
  - "traefik.http.routers.registry-ui.entrypoints=websecure"
  - "traefik.http.routers.registry-ui.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
registry-ui.example.com {
    reverse_proxy registry-ui:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop registry-ui
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf registry-ui-backup-$(date +%F).tar.gz ./data/registry-ui
   ```
3. Restart the container:
   ```bash
   docker start registry-ui
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop registry-ui && docker rm registry-ui
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf registry-ui-backup-YYYY-MM-DD.tar.gz -C ./data/registry-ui
   ```
3. Redeploy the stack via Dockhand.

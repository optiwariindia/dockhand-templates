# Portainer Dockhand Template

**Category:** Development  
**Default Image:** `portainer/portainer-ce:latest`

---

## 📖 Description
Making Docker & Kubernetes management easy with a modern Web UI.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `9000:9000`
* `9443:9443`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host path for Portainer database | `./data/portainer` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `portainer.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `portainer` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.portainer.rule=Host(`portainer.example.com`)"
  - "traefik.http.routers.portainer.entrypoints=websecure"
  - "traefik.http.routers.portainer.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
portainer.example.com {
    reverse_proxy portainer:9000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop portainer
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf portainer-backup-$(date +%F).tar.gz ./data/portainer
   ```
3. Restart the container:
   ```bash
   docker start portainer
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop portainer && docker rm portainer
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf portainer-backup-YYYY-MM-DD.tar.gz -C ./data/portainer
   ```
3. Redeploy the stack via Dockhand.

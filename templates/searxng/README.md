# SearXNG Dockhand Template

**Category:** AI  
**Default Image:** `searxng/searxng:latest`

---

## 📖 Description
Privacy-respecting, hackable metasearch engine aggregator.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `8080:8080`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `SEARXNG_BASE_URL` | Public domain or URL of SearXNG | `http://localhost:8080` |
| `DATA_PATH` | Host path for configuration files | `./data/searxng` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `searxng.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `searxng` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.searxng.rule=Host(`searxng.example.com`)"
  - "traefik.http.routers.searxng.entrypoints=websecure"
  - "traefik.http.routers.searxng.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
searxng.example.com {
    reverse_proxy searxng:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop searxng
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf searxng-backup-$(date +%F).tar.gz ./data/searxng
   ```
3. Restart the container:
   ```bash
   docker start searxng
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop searxng && docker rm searxng
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf searxng-backup-YYYY-MM-DD.tar.gz -C ./data/searxng
   ```
3. Redeploy the stack via Dockhand.

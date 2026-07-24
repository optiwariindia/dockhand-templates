# Beszel Dockhand Template

**Category:** Monitoring  
**Default Image:** `henrygd/beszel:latest`

---

## 📖 Description
Lightweight server monitoring hub with Docker statistics, alerts & charts.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `8090:8090`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host path for Beszel data storage | `./data/beszel` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `beszel.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `beszel` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.beszel.rule=Host(`beszel.example.com`)"
  - "traefik.http.routers.beszel.entrypoints=websecure"
  - "traefik.http.routers.beszel.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
beszel.example.com {
    reverse_proxy beszel:8090
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop beszel
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf beszel-backup-$(date +%F).tar.gz ./data/beszel
   ```
3. Restart the container:
   ```bash
   docker start beszel
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop beszel && docker rm beszel
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf beszel-backup-YYYY-MM-DD.tar.gz -C ./data/beszel
   ```
3. Redeploy the stack via Dockhand.

# Valkey Dockhand Template

**Category:** Infrastructure  
**Default Image:** `valkey/valkey:8-alpine`

---

## 📖 Description
High-performance open-source in-memory datastore (Redis fork).

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `6379:6379`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `VALKEY_PASSWORD` | Authentication password for Valkey server | `changeme123` |
| `DATA_PATH` | Host path for data storage | `./data/valkey` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `valkey.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `valkey` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.valkey.rule=Host(`valkey.example.com`)"
  - "traefik.http.routers.valkey.entrypoints=websecure"
  - "traefik.http.routers.valkey.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
valkey.example.com {
    reverse_proxy valkey:6379
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop valkey
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf valkey-backup-$(date +%F).tar.gz ./data/valkey
   ```
3. Restart the container:
   ```bash
   docker start valkey
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop valkey && docker rm valkey
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf valkey-backup-YYYY-MM-DD.tar.gz -C ./data/valkey
   ```
3. Redeploy the stack via Dockhand.

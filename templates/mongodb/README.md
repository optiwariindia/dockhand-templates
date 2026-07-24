# MongoDB Dockhand Template

**Category:** Infrastructure  
**Default Image:** `mongo:8`

---

## 📖 Description
High-performance document-oriented NoSQL database server.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `27017:27017`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `MONGO_INITDB_ROOT_USERNAME` | MongoDB root administrator username | `admin` |
| `MONGO_INITDB_ROOT_PASSWORD` | MongoDB root administrator password | `changeme123` |
| `DATA_PATH` | Host path for storing database persistence files | `./data/mongodb` |
| `TZ` | Container timezone setting | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `mongodb.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `mongodb` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.mongodb.rule=Host(`mongodb.example.com`)"
  - "traefik.http.routers.mongodb.entrypoints=websecure"
  - "traefik.http.routers.mongodb.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
mongodb.example.com {
    reverse_proxy mongodb:27017
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop mongodb
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf mongodb-backup-$(date +%F).tar.gz ./data/mongodb
   ```
3. Restart the container:
   ```bash
   docker start mongodb
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop mongodb && docker rm mongodb
   ```
2. Extract backup archive to `./data/mongodb`.
3. Redeploy the stack via Dockhand.

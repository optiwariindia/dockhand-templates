# Redis Dockhand Template

**Category:** Infrastructure  
**Default Image:** `redis:7-alpine`

---

## 📖 Description
In-memory data structure store used as database, cache, and message broker.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `6379:6379`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `REDIS_PASSWORD` | Authentication password for Redis client connections | `changeme123` |
| `DATA_PATH` | Persistence directory for RDB/AOF dumps | `./data/redis` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `redis.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `redis` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.redis.rule=Host(`redis.example.com`)"
  - "traefik.http.routers.redis.entrypoints=websecure"
  - "traefik.http.routers.redis.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
redis.example.com {
    reverse_proxy redis:6379
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop redis
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf redis-backup-$(date +%F).tar.gz ./data/redis
   ```
3. Restart the container:
   ```bash
   docker start redis
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop redis && docker rm redis
   ```
2. Extract backup archive to `./data/redis`.
3. Redeploy the stack via Dockhand.

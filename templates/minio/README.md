# MinIO Dockhand Template

**Category:** Infrastructure  
**Default Image:** `minio/minio:RELEASE.2024-11-07T00-52-20Z`

---

## 📖 Description
High-performance S3-compatible object storage server.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `9000:9000`
* `9001:9001`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `MINIO_ROOT_USER` | MinIO admin user/access key | `minioadmin` |
| `MINIO_ROOT_PASSWORD` | MinIO admin secret key (min 8 chars) | `minioadmin123` |
| `DATA_PATH` | Host directory for object storage data | `./data/minio` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `minio.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `minio` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.minio.rule=Host(`minio.example.com`)"
  - "traefik.http.routers.minio.entrypoints=websecure"
  - "traefik.http.routers.minio.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
minio.example.com {
    reverse_proxy minio:9000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop minio
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf minio-backup-$(date +%F).tar.gz ./data/minio
   ```
3. Restart the container:
   ```bash
   docker start minio
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop minio && docker rm minio
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf minio-backup-YYYY-MM-DD.tar.gz -C ./data/minio
   ```
3. Redeploy the stack via Dockhand.

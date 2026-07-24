# MariaDB Dockhand Template

**Category:** Infrastructure  
**Default Image:** `mariadb:11`

---

## 📖 Description
Fast, scalable, open-source relational database management system.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `3306:3306`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `MYSQL_ROOT_PASSWORD` | MariaDB root user password | `changeme123` |
| `MYSQL_DATABASE` | Default database name to create | `appdb` |
| `MYSQL_USER` | Non-root user to create | `appuser` |
| `MYSQL_PASSWORD` | Password for non-root user | `userpass123` |
| `DATA_PATH` | Host directory for data persistence | `./data/mariadb` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `mariadb.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `mariadb` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.mariadb.rule=Host(`mariadb.example.com`)"
  - "traefik.http.routers.mariadb.entrypoints=websecure"
  - "traefik.http.routers.mariadb.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
mariadb.example.com {
    reverse_proxy mariadb:3306
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop mariadb
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf mariadb-backup-$(date +%F).tar.gz ./data/mariadb
   ```
3. Restart the container:
   ```bash
   docker start mariadb
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop mariadb && docker rm mariadb
   ```
2. Extract backup archive to `./data/mariadb`.
3. Redeploy the stack via Dockhand.

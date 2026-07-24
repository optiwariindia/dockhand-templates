# MySQL Dockhand Template

**Category:** Infrastructure  
**Default Image:** `mysql:8.4`

---

## 📖 Description
World's most popular open-source relational database system.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `3306:3306`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `MYSQL_ROOT_PASSWORD` | MySQL root password | `changeme123` |
| `MYSQL_DATABASE` | Default initial database | `appdb` |
| `MYSQL_USER` | Standard user | `dbuser` |
| `MYSQL_PASSWORD` | Standard user password | `userpass123` |
| `DATA_PATH` | Data directory on host | `./data/mysql` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `mysql.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `mysql` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.mysql.rule=Host(`mysql.example.com`)"
  - "traefik.http.routers.mysql.entrypoints=websecure"
  - "traefik.http.routers.mysql.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
mysql.example.com {
    reverse_proxy mysql:3306
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop mysql
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf mysql-backup-$(date +%F).tar.gz ./data/mysql
   ```
3. Restart the container:
   ```bash
   docker start mysql
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop mysql && docker rm mysql
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf mysql-backup-YYYY-MM-DD.tar.gz -C ./data/mysql
   ```
3. Redeploy the stack via Dockhand.

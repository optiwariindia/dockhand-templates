# PostgreSQL Dockhand Template

**Category:** Infrastructure  
**Default Image:** `postgres:17-alpine`

---

## 📖 Description
Powerful, open-source object-relational database system.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `5432:5432`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `POSTGRES_USER` | Superuser username | `postgres` |
| `POSTGRES_PASSWORD` | Superuser password | `changeme123` |
| `POSTGRES_DB` | Default database name created upon startup | `appdb` |
| `DATA_PATH` | Host directory for data persistence | `./data/postgres` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `postgresql.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `postgresql` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.postgresql.rule=Host(`postgresql.example.com`)"
  - "traefik.http.routers.postgresql.entrypoints=websecure"
  - "traefik.http.routers.postgresql.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
postgresql.example.com {
    reverse_proxy postgresql:5432
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop postgresql
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf postgresql-backup-$(date +%F).tar.gz ./data/postgresql
   ```
3. Restart the container:
   ```bash
   docker start postgresql
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop postgresql && docker rm postgresql
   ```
2. Extract backup archive to `./data/postgresql`.
3. Redeploy the stack via Dockhand.

# PHP Environment (Om Prakash Tiwari) Dockhand Template

**Category:** Development  
**Default Image:** `optiwariindia/php:latest`

---

## 📖 Description
Custom PHP web application runtime container.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `8080:80`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `WEB_ROOT` | Host path for PHP application code | `./data/php` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `optiwari-php.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `optiwari-php` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.optiwari-php.rule=Host(`optiwari-php.example.com`)"
  - "traefik.http.routers.optiwari-php.entrypoints=websecure"
  - "traefik.http.routers.optiwari-php.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
optiwari-php.example.com {
    reverse_proxy optiwari-php:8080
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop optiwari-php
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf optiwari-php-backup-$(date +%F).tar.gz ./data/optiwari-php
   ```
3. Restart the container:
   ```bash
   docker start optiwari-php
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop optiwari-php && docker rm optiwari-php
   ```
2. Extract backup archive to `./data/optiwari-php`.
3. Redeploy the stack via Dockhand.

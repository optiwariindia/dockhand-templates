# NGINX Proxy Manager Dockhand Template

**Category:** Reverse Proxy  
**Default Image:** `jc21/nginx-proxy-manager:latest`

---

## 📖 Description
Intuitive web interface for NGINX proxying with free SSL certificates.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `80:80`
* `81:81`
* `443:443`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host directory for app data & database | `./data/npm` |
| `LETSENCRYPT_PATH` | Host directory for SSL certificates | `./data/npm/letsencrypt` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `nginx-proxy-manager.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `nginx-proxy-manager` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.nginx-proxy-manager.rule=Host(`nginx-proxy-manager.example.com`)"
  - "traefik.http.routers.nginx-proxy-manager.entrypoints=websecure"
  - "traefik.http.routers.nginx-proxy-manager.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
nginx-proxy-manager.example.com {
    reverse_proxy nginx-proxy-manager:80
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop nginx-proxy-manager
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf nginx-proxy-manager-backup-$(date +%F).tar.gz ./data/nginx-proxy-manager
   ```
3. Restart the container:
   ```bash
   docker start nginx-proxy-manager
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop nginx-proxy-manager && docker rm nginx-proxy-manager
   ```
2. Extract backup archive to `./data/nginx-proxy-manager`.
3. Redeploy the stack via Dockhand.

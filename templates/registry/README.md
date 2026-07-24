# Docker Registry Dockhand Template

**Category:** Development  
**Default Image:** `registry:2`

---

## 📖 Description
Stateless, highly scalable server application that stores and lets you distribute Docker images.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `5000:5000`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host directory for storing Docker image layers | `./data/registry` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `registry.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `registry` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.registry.rule=Host(`registry.example.com`)"
  - "traefik.http.routers.registry.entrypoints=websecure"
  - "traefik.http.routers.registry.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
registry.example.com {
    reverse_proxy registry:5000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop registry
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf registry-backup-$(date +%F).tar.gz ./data/registry
   ```
3. Restart the container:
   ```bash
   docker start registry
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop registry && docker rm registry
   ```
2. Extract backup archive to `./data/registry`.
3. Redeploy the stack via Dockhand.

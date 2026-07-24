# Uptime Kuma Dockhand Template

**Category:** Monitoring  
**Default Image:** `louislam/uptime-kuma:1`

---

## 📖 Description
A fancy, easy-to-use self-hosted monitoring tool.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `3001:3001`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host directory for Uptime Kuma SQLite database | `./data/uptime-kuma` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `uptime-kuma.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `uptime-kuma` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.uptime-kuma.rule=Host(`uptime-kuma.example.com`)"
  - "traefik.http.routers.uptime-kuma.entrypoints=websecure"
  - "traefik.http.routers.uptime-kuma.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
uptime-kuma.example.com {
    reverse_proxy uptime-kuma:3001
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop uptime-kuma
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf uptime-kuma-backup-$(date +%F).tar.gz ./data/uptime-kuma
   ```
3. Restart the container:
   ```bash
   docker start uptime-kuma
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop uptime-kuma && docker rm uptime-kuma
   ```
2. Extract backup archive to `./data/uptime-kuma`.
3. Redeploy the stack via Dockhand.

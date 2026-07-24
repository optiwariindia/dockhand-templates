# Pravah Realtime Sync (Om Prakash Tiwari) Dockhand Template

**Category:** Microservices  
**Default Image:** `optiwariindia/pravah:latest`

---

## 📖 Description
Real-time event synchronization engine and broadcasting server.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `3000:3000`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `PORT` | Application listening port | `3000` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `pravah.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `pravah` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.pravah.rule=Host(`pravah.example.com`)"
  - "traefik.http.routers.pravah.entrypoints=websecure"
  - "traefik.http.routers.pravah.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
pravah.example.com {
    reverse_proxy pravah:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop pravah
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf pravah-backup-$(date +%F).tar.gz ./data/pravah
   ```
3. Restart the container:
   ```bash
   docker start pravah
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop pravah && docker rm pravah
   ```
2. Extract backup archive to `./data/pravah`.
3. Redeploy the stack via Dockhand.

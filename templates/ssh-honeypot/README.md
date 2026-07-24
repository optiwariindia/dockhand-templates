# SSH Honeypot (Om Prakash Tiwari) Dockhand Template

**Category:** Security  
**Default Image:** `optiwariindia/ssh-honeypot:latest`

---

## 📖 Description
SSH honeypot service designed to detect, trap, and log intruder interactions.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `2222:22`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `LOG_PATH` | Host path for storing intruder session logs | `./data/ssh-honeypot` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `ssh-honeypot.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `ssh-honeypot` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.ssh-honeypot.rule=Host(`ssh-honeypot.example.com`)"
  - "traefik.http.routers.ssh-honeypot.entrypoints=websecure"
  - "traefik.http.routers.ssh-honeypot.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
ssh-honeypot.example.com {
    reverse_proxy ssh-honeypot:2222
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop ssh-honeypot
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf ssh-honeypot-backup-$(date +%F).tar.gz ./data/ssh-honeypot
   ```
3. Restart the container:
   ```bash
   docker start ssh-honeypot
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop ssh-honeypot && docker rm ssh-honeypot
   ```
2. Extract backup archive to `./data/ssh-honeypot`.
3. Redeploy the stack via Dockhand.

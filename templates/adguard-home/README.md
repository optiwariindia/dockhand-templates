# AdGuard Home Dockhand Template

**Category:** Networking  
**Default Image:** `adguard/adguardhome:latest`

---

## 📖 Description
Network-wide software for blocking ads & tracking and controlling DNS requests.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `53:53/tcp`
* `53:53/udp`
* `80:80/tcp`
* `3000:3000/tcp`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `CONFIG_PATH` | Host directory for AdGuardHome.yaml | `./config/adguard` |
| `DATA_PATH` | Host directory for DNS query logs & stats | `./data/adguard` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `adguard-home.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `adguard-home` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.adguard-home.rule=Host(`adguard-home.example.com`)"
  - "traefik.http.routers.adguard-home.entrypoints=websecure"
  - "traefik.http.routers.adguard-home.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
adguard-home.example.com {
    reverse_proxy adguard-home:53
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop adguard-home
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf adguard-home-backup-$(date +%F).tar.gz ./data/adguard-home
   ```
3. Restart the container:
   ```bash
   docker start adguard-home
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop adguard-home && docker rm adguard-home
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf adguard-home-backup-YYYY-MM-DD.tar.gz -C ./data/adguard-home
   ```
3. Redeploy the stack via Dockhand.

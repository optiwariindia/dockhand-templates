# Pi-hole Dockhand Template

**Category:** Networking  
**Default Image:** `pihole/pihole:latest`

---

## 📖 Description
DNS sinkhole that protects your devices from unwanted content without extra software.

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

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `WEBPASSWORD` | Web admin console password | `changeme123` |
| `FTLCONF_LOCAL_IPV4` | Static IP of host running Pi-hole | `192.168.1.100` |
| `DATA_PATH` | Host path for configuration files | `./data/pihole` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `pi-hole.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `pi-hole` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.pi-hole.rule=Host(`pi-hole.example.com`)"
  - "traefik.http.routers.pi-hole.entrypoints=websecure"
  - "traefik.http.routers.pi-hole.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
pi-hole.example.com {
    reverse_proxy pi-hole:53
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop pi-hole
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf pi-hole-backup-$(date +%F).tar.gz ./data/pi-hole
   ```
3. Restart the container:
   ```bash
   docker start pi-hole
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop pi-hole && docker rm pi-hole
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf pi-hole-backup-YYYY-MM-DD.tar.gz -C ./data/pi-hole
   ```
3. Redeploy the stack via Dockhand.

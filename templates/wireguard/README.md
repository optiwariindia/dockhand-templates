# WireGuard Dockhand Template

**Category:** Networking  
**Default Image:** `lscr.io/linuxserver/wireguard:latest`

---

## 📖 Description
Extremely simple yet fast and modern VPN server.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `51820:51820/udp`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `PUID` | Process User ID | `1000` |
| `PGID` | Process Group ID | `1000` |
| `SERVERURL` | Public domain or IP address for clients to connect | `wireguard.example.com` |
| `SERVERPORT` | External UDP Port | `51820` |
| `PEERS` | Number of client configuration files to generate | `5` |
| `DATA_PATH` | Host directory for generated configs & keys | `./data/wireguard` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `wireguard.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `wireguard` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.wireguard.rule=Host(`wireguard.example.com`)"
  - "traefik.http.routers.wireguard.entrypoints=websecure"
  - "traefik.http.routers.wireguard.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
wireguard.example.com {
    reverse_proxy wireguard:51820
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop wireguard
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf wireguard-backup-$(date +%F).tar.gz ./data/wireguard
   ```
3. Restart the container:
   ```bash
   docker start wireguard
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop wireguard && docker rm wireguard
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf wireguard-backup-YYYY-MM-DD.tar.gz -C ./data/wireguard
   ```
3. Redeploy the stack via Dockhand.

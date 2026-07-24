# NATS Dockhand Template

**Category:** Infrastructure  
**Default Image:** `nats:latest`

---

## 📖 Description
Cloud-native microservices messaging system and JetStream persistence engine.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `4222:4222`
* `8222:8222`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host path for JetStream storage | `./data/nats` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `nats.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `nats` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.nats.rule=Host(`nats.example.com`)"
  - "traefik.http.routers.nats.entrypoints=websecure"
  - "traefik.http.routers.nats.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
nats.example.com {
    reverse_proxy nats:4222
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop nats
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf nats-backup-$(date +%F).tar.gz ./data/nats
   ```
3. Restart the container:
   ```bash
   docker start nats
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop nats && docker rm nats
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf nats-backup-YYYY-MM-DD.tar.gz -C ./data/nats
   ```
3. Redeploy the stack via Dockhand.

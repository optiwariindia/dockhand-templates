# RabbitMQ Dockhand Template

**Category:** Infrastructure  
**Default Image:** `rabbitmq:3-management-alpine`

---

## 📖 Description
Robust, widely deployed open-source message broker.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `5672:5672`
* `15672:15672`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `RABBITMQ_DEFAULT_USER` | Administrator login username | `admin` |
| `RABBITMQ_DEFAULT_PASS` | Administrator login password | `changeme123` |
| `DATA_PATH` | Host path for RabbitMQ data persistence | `./data/rabbitmq` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `rabbitmq.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `rabbitmq` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.rabbitmq.rule=Host(`rabbitmq.example.com`)"
  - "traefik.http.routers.rabbitmq.entrypoints=websecure"
  - "traefik.http.routers.rabbitmq.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
rabbitmq.example.com {
    reverse_proxy rabbitmq:5672
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop rabbitmq
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf rabbitmq-backup-$(date +%F).tar.gz ./data/rabbitmq
   ```
3. Restart the container:
   ```bash
   docker start rabbitmq
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop rabbitmq && docker rm rabbitmq
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf rabbitmq-backup-YYYY-MM-DD.tar.gz -C ./data/rabbitmq
   ```
3. Redeploy the stack via Dockhand.

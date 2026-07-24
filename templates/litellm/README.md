# LiteLLM Dockhand Template

**Category:** AI  
**Default Image:** `ghcr.io/berriai/litellm:main-latest`

---

## 📖 Description
Unified I/O proxy for 100+ LLM APIs with load balancing & tracking.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `4000:4000`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `LITELLM_MASTER_KEY` | Admin API key for proxy authentication | `sk-1234masterkey` |
| `CONFIG_PATH` | Directory containing config.yaml | `./config/litellm` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `litellm.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `litellm` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.litellm.rule=Host(`litellm.example.com`)"
  - "traefik.http.routers.litellm.entrypoints=websecure"
  - "traefik.http.routers.litellm.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
litellm.example.com {
    reverse_proxy litellm:4000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop litellm
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf litellm-backup-$(date +%F).tar.gz ./data/litellm
   ```
3. Restart the container:
   ```bash
   docker start litellm
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop litellm && docker rm litellm
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf litellm-backup-YYYY-MM-DD.tar.gz -C ./data/litellm
   ```
3. Redeploy the stack via Dockhand.

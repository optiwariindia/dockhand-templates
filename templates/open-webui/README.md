# Open WebUI Dockhand Template

**Category:** AI  
**Default Image:** `ghcr.io/open-webui/open-webui:main`

---

## 📖 Description
User-friendly WebUI for Ollama, OpenAI, and custom LLM inference endpoints.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Host path configured for persistent volumes (if required).

---

## 🔌 Ports
* `3000:8080`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `OLLAMA_BASE_URL` | Endpoint URL for connected Ollama instance | `http://ollama:11434` |
| `DATA_PATH` | Host directory for WebUI persistent data | `./data/open-webui` |
| `WEBUI_SECRET_KEY` | Session encryption key | `supersecretkey123` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `open-webui.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `open-webui` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.open-webui.rule=Host(`open-webui.example.com`)"
  - "traefik.http.routers.open-webui.entrypoints=websecure"
  - "traefik.http.routers.open-webui.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
open-webui.example.com {
    reverse_proxy open-webui:3000
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop open-webui
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf open-webui-backup-$(date +%F).tar.gz ./data/open-webui
   ```
3. Restart the container:
   ```bash
   docker start open-webui
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop open-webui && docker rm open-webui
   ```
2. Extract backup archive to `./data/open-webui`.
3. Redeploy the stack via Dockhand.

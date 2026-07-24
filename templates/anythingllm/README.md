# AnythingLLM Dockhand Template

**Category:** AI  
**Default Image:** `mintplexlabs/anythingllm:latest`

---

## 📖 Description
All-in-one AI enterprise workspace for RAG, custom AI agents, and documents.

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
| `STORAGE_DIR` | Host path for vector databases and documents | `./data/anythingllm` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `anythingllm.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `anythingllm` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.anythingllm.rule=Host(`anythingllm.example.com`)"
  - "traefik.http.routers.anythingllm.entrypoints=websecure"
  - "traefik.http.routers.anythingllm.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
anythingllm.example.com {
    reverse_proxy anythingllm:3001
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop anythingllm
   ```
2. Archive persistent volumes:
   ```bash
   tar -czvf anythingllm-backup-$(date +%F).tar.gz ./data/anythingllm
   ```
3. Restart the container:
   ```bash
   docker start anythingllm
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop anythingllm && docker rm anythingllm
   ```
2. Extract backup archive to `./data/anythingllm`.
3. Redeploy the stack via Dockhand.

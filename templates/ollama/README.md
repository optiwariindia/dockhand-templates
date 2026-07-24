# Ollama Dockhand Template

**Category:** AI  
**Default Image:** `ollama/ollama:latest`

---

## 📖 Description
Get up and running with Llama 3, Mistral, Gemma, and other LLMs locally.

---

## 📋 Requirements
* Docker Engine 20.10+
* Docker Compose v2+
* Dockhand or Portainer management UI
* Persistent storage path configured on the host machine.

---

## 🔌 Ports
* `11434:11434`

---

## ⚙️ Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DATA_PATH` | Host directory to store downloaded model weights | `./data/ollama` |
| `TZ` | Container timezone | `UTC` |

---

## 🌐 Reverse Proxy Example

### NGINX Proxy Manager
1. Forward host domain (e.g. `ollama.example.com`) to container IP/hostname on the internal port.
2. Request a Let's Encrypt SSL certificate with HTTP/2 enabled.

### Traefik
Add labels to `ollama` in `docker-compose.yml`:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.ollama.rule=Host(`ollama.example.com`)"
  - "traefik.http.routers.ollama.entrypoints=websecure"
  - "traefik.http.routers.ollama.tls.certresolver=myresolver"
```

### Caddy
Add to your `Caddyfile`:
```caddy
ollama.example.com {
    reverse_proxy ollama:11434
}
```

---

## 💾 Backup Instructions

1. Stop the container to ensure data consistency:
   ```bash
   docker stop ollama
   ```
2. Archive the host persistent directory specified by `${DATA_PATH}`:
   ```bash
   tar -czvf ollama-backup-$(date +%F).tar.gz ./data/ollama
   ```
3. Restart the container:
   ```bash
   docker start ollama
   ```

---

## 🔄 Restore Instructions

1. Stop and remove the existing container:
   ```bash
   docker stop ollama && docker rm ollama
   ```
2. Extract your backup archive to the designated `${DATA_PATH}`:
   ```bash
   tar -xzvf ollama-backup-YYYY-MM-DD.tar.gz -C ./data/ollama
   ```
3. Redeploy the stack via Dockhand.

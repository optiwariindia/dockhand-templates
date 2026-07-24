# Dockhand Template Repository

Welcome to the official **Dockhand Template Repository**. This collection provides production-ready, standardized Docker Compose templates for hosting databases, reverse proxies, AI services, monitoring tools, networking utilities, development tools, and self-hosted apps in Dockhand or Portainer.

---

## 📁 Repository Structure

```text
dockhand-templates/
├── index.json                 # Auto-generated Portainer v2 / Dockhand global template index
├── build_index.py             # Python script to compile individual template.json files
├── templates/                 # Modular template directory
│   ├── mongodb/
│   │   ├── docker-compose.yml # Docker compose configuration
│   │   ├── template.json      # Dockhand metadata & environment variable schema
│   │   ├── icon.svg           # High-resolution vector icon
│   │   └── README.md          # Comprehensive deployment & management guide
│   ├── postgresql/
│   ├── redis/
│   └── ...
└── README.md
```

---

## 🏷️ Main Categories & Included Templates

### 🛠️ Infrastructure
* **MongoDB** - Document-oriented NoSQL Database
* **PostgreSQL** - Advanced Relational Database Engine
* **MariaDB** - Fast, reliable MySQL fork
* **MySQL** - Popular open-source Relational Database
* **Redis** - In-memory key-value data structure store
* **Valkey** - High-performance open-source Redis alternative
* **NATS** - Cloud-native messaging and streaming system
* **RabbitMQ** - Enterprise message broker
* **MinIO** - High-performance S3-compatible Object Storage

### 🌐 Reverse Proxy
* **NGINX Proxy Manager** - Easy web UI for NGINX proxying and SSL management
* **Traefik** - Modern cloud-native edge router and reverse proxy
* **Caddy** - Fast, powerful web server with automatic HTTPS

### 🤖 AI & Machine Learning
* **Ollama** - Run large language models (LLMs) locally
* **Open WebUI** - User-friendly web interface for Ollama & OpenAI-compatible APIs
* **AnythingLLM** - Full-stack enterprise AI application & RAG platform
* **SearXNG** - Privacy-respecting metasearch engine
* **LiteLLM** - Unified proxy for 100+ LLM APIs

### 📊 Monitoring & Logging
* **Grafana** - Analytics and interactive visualization dashboard
* **Prometheus** - Time-series metric collection and alerting platform
* **Loki** - Log aggregation system designed for performance
* **Uptime Kuma** - Modern self-hosted uptime monitoring tool
* **Beszel** - Lightweight server monitoring dashboard

### 🔒 Networking & Privacy
* **Tailscale** - Zero-config mesh VPN based on WireGuard
* **Headscale** - Open-source self-hosted implementation of the Tailscale control server
* **WireGuard** - High-performance, modern VPN server
* **AdGuard Home** - Network-wide DNS ad and tracker blocking
* **Pi-hole** - Network-wide sinkhole DNS server

### 💻 Development Tools
* **Portainer** - Lightweight container management platform
* **Dockge** - Modern, easy-to-use Docker Compose manager
* **Gitea** - Lightweight DevOps Git service
* **Forgejo** - Self-hosted software development platform (Gitea fork)
* **Registry** - Private Docker Container Image Registry (v2)
* **Registry UI** - Web interface for Docker Registry

### 🧰 Utilities & Productivity
* **Watchtower** - Automatic Docker container updater
* **Dozzle** - Real-time Docker container log viewer
* **Filebrowser** - Web-based file management interface
* **Homepage** - Highly customizable modern dashboard
* **Stirling PDF** - Powerful local PDF manipulation suite
* **Vaultwarden** - Lightweight Bitwarden-compatible password manager in Rust

---

## ⚡ Standard Environment Variables

All templates adhere to a standardized variable naming convention for consistency across installations:

| Variable | Description | Standard Default |
| :--- | :--- | :--- |
| `TZ` | Container Timezone | `UTC` or `Asia/Kolkata` |
| `PUID` | Process User ID | `1000` |
| `PGID` | Process Group ID | `1000` |
| `DATA_PATH` | Host persistent volume directory | `./data/<service>` |
| `PORT` | Primary service HTTP/TCP port | Service-specific standard port |
| `DOMAIN` | FQDN or hostname for web apps | `app.local` |
| `PASSWORD` | Admin / service password | Prompted / UI configured |

---

## 🔄 Building / Updating `index.json`

To rebuild the root `index.json` catalog after adding or modifying templates, run:

```bash
python3 build_index.py
```

---

## ✍️ Author & Maintenance

Lead Engineer: **Om Prakash Tiwari**

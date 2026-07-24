# Dockhand Template Repository

[![39 Templates](https://img.shields.io/badge/Templates-39%20Available-brightgreen.svg)](#-included-templates)
[![Dockhand Compatible](https://img.shields.io/badge/Dockhand-Compatible-blue.svg)](#-how-to-use-in-dockhand)
[![Portainer v2](https://img.shields.io/badge/Portainer-v2%20Schema-orange.svg)](#-how-to-use-in-dockhand)

Welcome to the official **Dockhand Template Repository**. This collection provides production-ready, standardized Docker Compose templates with auto-configurable environment variables, persistent volumes, SVG icons, and deployment guides.

---

## 🚀 How to Use in Dockhand

### Method 1: Adding as Custom App Template Catalog (Recommended)

1. Open your **Dockhand** Web UI.
2. Navigate to **Settings** -> **App Templates** (or **App Catalog**).
3. Set the **URL** input to:
   ```text
   https://raw.githubusercontent.com/optiwariindia/dockhand-templates/main/index.json
   ```
4. Click **Save** or **Fetch Templates**.
5. Go to the **Templates** section in Dockhand to instantly browse, search, and deploy any of the **39+ templates** with pre-filled forms.

---

### Method 2: Deploying Individual Stacks via URL

If you want to deploy a single application stack directly in Dockhand:
1. In Dockhand, select **New Stack** -> **From Repository**.
2. Set **Repository URL**: `https://github.com/optiwariindia/dockhand-templates`
3. Set **Compose Path**: `templates/<template-name>/docker-compose.yml`  
   *(e.g., `templates/mongodb/docker-compose.yml` or `templates/ollama/docker-compose.yml`)*
4. Fill in environment variables and click **Deploy Stack**.

---

## 📂 Repository Layout

```text
dockhand-templates/
├── index.json                 # Global Portainer v2 / Dockhand template catalog
├── build_index.py             # Python compiler script for index.json
├── templates/                 # Modular template directory
│   ├── mongodb/
│   │   ├── docker-compose.yml # Standardized Docker Compose file
│   │   ├── template.json      # Dockhand UI form schema & metadata
│   │   ├── icon.svg           # High-resolution vector icon
│   │   └── README.md          # Comprehensive deployment & management guide
│   ├── postgresql/
│   ├── redis/
│   └── ... (39 total)
└── README.md
```

---

## 🏷️ Included Templates

### 🛠️ Infrastructure (9)
* **MongoDB** - Document-oriented NoSQL Database (`mongo:8`)
* **PostgreSQL** - Relational Database Engine (`postgres:17-alpine`)
* **Redis** - In-memory key-value data structure store (`redis:7-alpine`)
* **Valkey** - Open-source Redis alternative (`valkey/valkey:8-alpine`)
* **MariaDB** - Fast MySQL fork database (`mariadb:11`)
* **MySQL** - Relational Database Server (`mysql:8.4`)
* **RabbitMQ** - Enterprise Message Broker with Management UI (`rabbitmq:3-management-alpine`)
* **MinIO** - S3-compatible Object Storage Server (`minio/minio:latest`)
* **NATS** - Cloud-native messaging & JetStream engine (`nats:latest`)

### 🌐 Reverse Proxy (3)
* **NGINX Proxy Manager** - Reverse proxy UI with auto Let's Encrypt SSL (`jc21/nginx-proxy-manager:latest`)
* **Traefik** - Cloud-native edge router (`traefik:v3.1`)
* **Caddy** - Enterprise web server with automatic HTTPS (`caddy:2-alpine`)

### 🤖 AI & Machine Learning (5)
* **Ollama** - Run LLMs locally (`ollama/ollama:latest`)
* **Open WebUI** - Web interface for Ollama & OpenAI APIs (`ghcr.io/open-webui/open-webui:main`)
* **AnythingLLM** - Enterprise RAG & AI Workspace (`mintplexlabs/anythingllm:latest`)
* **SearXNG** - Privacy metasearch engine (`searxng/searxng:latest`)
* **LiteLLM** - Proxy for 100+ LLM APIs (`ghcr.io/berriai/litellm:main-latest`)

### 📊 Monitoring & Observability (5)
* **Grafana** - Data visualization dashboards (`grafana/grafana:latest`)
* **Prometheus** - Time-series metrics engine (`prom/prometheus:latest`)
* **Loki** - High-performance log aggregation (`grafana/loki:latest`)
* **Uptime Kuma** - Modern self-hosted status & uptime monitoring (`louislam/uptime-kuma:1`)
* **Beszel** - Lightweight server & container monitoring (`henrygd/beszel:latest`)

### 🔒 Networking & Privacy (5)
* **Tailscale** - Zero-config mesh VPN (`tailscale/tailscale:latest`)
* **Headscale** - Open-source Tailscale control server (`headscale/headscale:latest`)
* **WireGuard** - High-speed modern VPN (`lscr.io/linuxserver/wireguard:latest`)
* **AdGuard Home** - Network-wide ad & tracker blocking DNS (`adguard/adguardhome:latest`)
* **Pi-hole** - Network-wide DNS sinkhole (`pihole/pihole:latest`)

### 💻 Development Tools (6)
* **Portainer** - Container management platform (`portainer/portainer-ce:latest`)
* **Dockge** - Reactive Docker Compose manager (`louislam/dockge:1`)
* **Gitea** - Lightweight self-hosted Git service (`gitea/gitea:latest`)
* **Forgejo** - Community-driven Git platform (`codeberg.org/forgejo/forgejo:9`)
* **Docker Registry** - Private Container Image Registry (`registry:2`)
* **Registry UI** - Web interface for Docker Registry (`joxit/docker-registry-ui:latest`)

### 🧰 Utilities & Productivity (6)
* **Watchtower** - Automatic Docker container updater (`containrrr/watchtower:latest`)
* **Dozzle** - Real-time Docker log viewer (`amir20/dozzle:latest`)
* **FileBrowser** - Web-based file manager (`filebrowser/filebrowser:latest`)
* **Homepage** - Modern customizable application dashboard (`ghcr.io/gethomepage/homepage:latest`)
* **Stirling PDF** - Powerful local PDF suite (`frooodle/s-pdf:latest`)
* **Vaultwarden** - Bitwarden-compatible password manager (`vaultwarden/server:latest`)

---

## ⚡ Standardized Variables

All templates use uniform, intuitive variable names:

| Variable | Description | Standard Default |
| :--- | :--- | :--- |
| `TZ` | Container Timezone | `UTC` |
| `PUID` | Process User ID | `1000` |
| `PGID` | Process Group ID | `1000` |
| `DATA_PATH` | Host path for persistent storage | `./data/<service>` |
| `CONFIG_PATH` | Host path for configuration files | `./config/<service>` |

---

## 🛠️ Maintaining & Rebuilding the Catalog

To add a new template or modify an existing template:
1. Edit or add the template directory in `templates/<new-service>/`.
2. Run the build script to update `index.json`:
   ```bash
   python3 build_index.py
   ```
3. Commit and push to `main`.

---

## ✍️ Author & Maintenance

Lead Engineer: **Om Prakash Tiwari**  
Repository: [optiwariindia/dockhand-templates](https://github.com/optiwariindia/dockhand-templates)

# Dockhand Template Repository

[![69 Templates](https://img.shields.io/badge/Templates-69%20Available-brightgreen.svg)](#-included-templates)
[![Dockhand Compatible](https://img.shields.io/badge/Dockhand-Compatible-blue.svg)](#-how-to-use-in-dockhand)
[![Portainer v2](https://img.shields.io/badge/Portainer-v2%20Schema-orange.svg)](#-how-to-use-in-dockhand)

Welcome to the official **Dockhand Template Repository**. This collection provides production-ready, standardized Docker Compose templates with auto-configurable environment variables, persistent volumes, SVG icons, and deployment guides — featuring both essential open-source software and **Om Prakash Tiwari's custom microservices suite**.

---

## 🚀 How to Use in Dockhand / Portainer

### Method 1: Adding as Custom App Template Catalog (Recommended)

1. Open your **Dockhand** or **Portainer** Web UI.
2. Navigate to **Settings** -> **App Templates** (or **App Catalog**).
3. Set the **URL** input to either of the following raw GitHub JSON URLs:
   - **`index.json` (Primary):**
     ```text
     https://raw.githubusercontent.com/optiwariindia/dockhand-templates/main/index.json
     ```
   - **`templates.json` (Alternative):**
     ```text
     https://raw.githubusercontent.com/optiwariindia/dockhand-templates/main/templates.json
     ```
4. Click **Save** or **Fetch Templates**.
5. Go to the **Templates** section in Dockhand/Portainer to instantly browse, search, and deploy any of the **69 templates** with pre-filled forms.

---

### Method 2: Deploying Individual Stacks via URL

If you want to deploy a single application stack directly in Dockhand:
1. In Dockhand, select **New Stack** -> **From Repository**.
2. Set **Repository URL**: `https://github.com/optiwariindia/dockhand-templates`
3. Set **Compose Path**: `templates/<template-name>/docker-compose.yml`  
   *(e.g., `templates/vscode-tunnel/docker-compose.yml` or `templates/mongodb/docker-compose.yml`)*
4. Fill in environment variables and click **Deploy Stack**.

---

## 📂 Repository Layout

```text
dockhand-templates/
├── index.json                 # Global Portainer v2 / Dockhand template catalog
├── templates.json             # Alias template catalog for Portainer/Dockhand compatibility
├── build_index.py             # Python compiler script for catalog indexes
├── templates/                 # Modular template directory
│   ├── mongodb/
│   ├── vscode-tunnel/
│   ├── bizbandhan-trace/
│   └── ... (69 total)
└── README.md
```

---

## 🏷️ Included Templates (69 Total)

### 🌟 Om Prakash Tiwari Apps & Microservices Suite (30)
* **VS Code Tunnel** (`optiwariindia/vscode-tunnel`) - Web-based VS Code remote IDE tunnel
* **BizBandhan Trace RUM** (`optiwariindia/bizbandhan-trace`) - OpenTelemetry-native Real-User Monitoring ingestion
* **Pravah Go SSE Server** (`optiwariindia/pravah-go`) - High-throughput SSE application sync in Go
* **Pravah Realtime Sync** (`optiwariindia/pravah`) - Real-time event broadcasting engine
* **Whatsmeow Listener** (`optiwariindia/whatsmeow`) - Lightweight WhatsApp event listener API
* **ExRate API** (`optiwariindia/exrate`) - Exchange rate API with daily caching
* **Location IP API** (`optiwariindia/location-ip`) - Whois IP address & country code lookup service
* **Address Options API** (`optiwariindia/address-options`) - Countries, states, & cities API dataset
* **SSH Honeypot** (`optiwariindia/ssh-honeypot`) - SSH intruder decoy & security logging service
* **LiveReload Server** (`optiwariindia/livereload`) - Auto-reload browser sync for Docker environments
* **Transcoder API** (`optiwariindia/transcoder`) - Video & audio media transcoding service
* **UUID Go Generator** (`optiwariindia/uuid-go`) - High-performance UUID generator in Go
* **GetCN Inspector** (`optiwariindia/getcn`) - SSL Certificate Common Name inspector
* **Get-PTR Resolver** (`optiwariindia/get-ptr`) - Reverse DNS PTR record lookup microservice
* **Email Validator API** (`optiwariindia/email-validator`) - Email syntax, MX, & deliverability checker
* **Validator Email Service** (`optiwariindia/validator-email`) - High-speed email validation microservice
* **Website Validator** (`optiwariindia/validator-website`) - Website status & SSL validator
* **CAPTCHA Service** (`optiwariindia/captcha`) - CAPTCHA image generation & token validation API
* **PDF Generator** (`optiwariindia/pdf`) - HTML-to-PDF compilation microservice
* **Excel Microservice** (`optiwariindia/excel`) - Excel file parsing & data transformation API
* **Coming Soon Server** (`optiwariindia/commingsoon`) - Lightweight maintenance / landing page
* **SSE Broadcasting Server** (`optiwariindia/sse-server`) - Server-Sent Events broadcasting hub
* **Email Template Service** (`optiwariindia/email-template`) - HTML Email template renderer & previewer
* **Express Twig Mailer** (`optiwariindia/express-twig-mailer`) - Express & Twig mail dispatch service
* **API Gateway** (`optiwariindia/gateway`) - Lightweight routing gateway microservice
* **OpenTelemetry Collector** (`optiwariindia/otel`) - OpenTelemetry metrics & traces pipeline
* **React Application Server** (`optiwariindia/react-server`) - React web app server & static asset host
* **Express Environment** (`optiwariindia/express`) - Node.js Express application container
* **PHP Environment** (`optiwariindia/php`) - Custom PHP web application runtime container
* **Gulp Runner** (`optiwariindia/gulp-runner`) - Gulp task runner container environment

---

### 🛠️ Infrastructure (9)
* **MongoDB** - Document NoSQL Database (`mongo:8`)
* **PostgreSQL** - Relational Database Engine (`postgres:17-alpine`)
* **Redis** - In-memory key-value data store (`redis:7-alpine`)
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
* **Ollama** - Local LLM inference server (`ollama/ollama:latest`)
* **Open WebUI** - Web UI for Ollama & OpenAI APIs (`ghcr.io/open-webui/open-webui:main`)
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

## ✍️ Author & Maintenance

Lead Engineer: **Om Prakash Tiwari**  
Repository: [optiwariindia/dockhand-templates](https://github.com/optiwariindia/dockhand-templates)

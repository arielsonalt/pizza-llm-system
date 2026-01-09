# ============================
# Project configuration
# ============================
DOCKER_USER := arielson
VERSION ?= latest

API_GATEWAY_IMAGE := $(DOCKER_USER)/pizza-api-gateway:$(VERSION)
AGENT_ORCH_IMAGE := $(DOCKER_USER)/pizza-agent-orchestrator:$(VERSION)
RAG_SERVICE_IMAGE := $(DOCKER_USER)/pizza-rag-service:$(VERSION)
MCP_TOOLS_IMAGE := $(DOCKER_USER)/pizza-mcp-tools:$(VERSION)
UI_STREAMLIT_IMAGE := $(DOCKER_USER)/pizza-ui-streamlit:$(VERSION)

# ============================
# Build images
# ============================
build:
	docker build -t $(API_GATEWAY_IMAGE) apps/api-gateway/app
	docker build -t $(AGENT_ORCH_IMAGE) apps/agent-orchestrator/app
	docker build -t $(RAG_SERVICE_IMAGE) apps/rag-service/app
	docker build -t $(MCP_TOOLS_IMAGE) apps/mcp-tools-server/app
	docker build -t $(UI_STREAMLIT_IMAGE) apps/ui-streamlit/app

# ============================
# Push images
# ============================
push:
	docker push $(API_GATEWAY_IMAGE)
	docker push $(AGENT_ORCH_IMAGE)
	docker push $(RAG_SERVICE_IMAGE)
	docker push $(MCP_TOOLS_IMAGE)
	docker push $(UI_STREAMLIT_IMAGE)

# ============================
# Build + Push
# ============================
release: build push

# ============================
# Local development
# ============================
up:
	docker compose -f infra/docker-compose.yml up -d

down:
	docker compose -f infra/docker-compose.yml down

logs:
	docker compose -f infra/docker-compose.yml logs -f

# ============================
# Utilities
# ============================
ps:
	docker compose -f infra/docker-compose.yml ps

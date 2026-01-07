# pizzeria LLM System 🍕

## Core

This project aims to build a **Large Language Model (LLM)–based system** integrated for a **fictional pizzeria**.  
The main objective is to provide **end-to-end customer service for pizza ordering via chat**, replacing or augmenting human attendants.

The system uses **AI agents** to analyze customer intent, guide conversations, answer questions, handle menu exploration, manage delivery constraints, and **drive the customer from the first interaction until the order is completed**.

The solution is designed to simulate a real-world production environment for conversational commerce.

---

## Project Goals

- Provide an **AI-driven chat experience** for pizza ordering
- Automate customer service flows traditionally handled by humans
- Support menu browsing, order creation, delivery validation, and payment steps
- Enable integration with external systems via standardized tool protocols
- Serve as a **reference architecture** for LLM-powered customer service systems

---

## Key Characteristics

- Fully **agent-based architecture**
- Clear separation of concerns using **microservices**
- Deterministic conversational flows using **state machines**
- Retrieval-Augmented Generation (RAG) for accurate menu and policy responses
- Designed for **scalability and cloud-native deployment**

---

## Technologies Used

- **Python**
- **FastAPI** – REST APIs and service communication
- **LangChain** – Agent orchestration and tool calling
- **LangGraph** – Stateful conversational workflows
- **LlamaIndex** – RAG (Retrieval-Augmented Generation)
- **MCP (Model Context Protocol)** – Standardized tool interface
- **Docker** – Containerization
- **Kubernetes** – Orchestration and scaling
- **PostgreSQL / Vector Stores** – Data and embeddings
- **OpenTelemetry** – Observability and tracing

---

## Architecture Overview

The system is composed of multiple independent services:

- **API Gateway**
  - Entry point for clients (web, mobile, chat)
  - Routes requests to the agent orchestrator

- **Agent Orchestrator**
  - Hosts LangChain agents
  - Controls conversation flow using LangGraph
  - Decides when to call tools or RAG services

- **RAG Service**
  - Indexes menu, allergens, policies, and delivery zones
  - Provides grounded answers to agents

- **MCP Tools Server**
  - Exposes business capabilities such as:
    - Menu access
    - Order creation
    - Delivery validation
    - Payment handling

---

## Recommended Versions

- **Python version:**  
  ```text
  >= 3.11 and < 3.12

## 🚧 Under active development
> - This project is currently being built and refined.
> - The focus is on correctness, architectural clarity, and production-readiness rather than rapid prototyping.

## Use Cases
- Conversational pizza ordering
- AI-powered customer support
- LLM + RAG reference implementation
- Agent-based commerce workflows
- Educational and architectural demonstration project
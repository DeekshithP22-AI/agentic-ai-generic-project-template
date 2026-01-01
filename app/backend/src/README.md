# `src` – Service Source Code

This folder contains **all the backend service code** for the Agentic AI Platform.  
It is the main codebase for the `backend` service.

---

## Structure Overview

- **agents/** – Contains all individual agents. Each agent has:
  - Its **own graph** (workflow), configuration, and prompts.
  - Prompts include goals, system messages, constraints, and templates.
  
- **api/** – Defines HTTP endpoints (FastAPI routes), including:
  - Versioned APIs (`v1/` folder).
  - Routes, schemas, dependency injections, and health checks.

- **app/** – Core backend logic:
  - `main.py` is the entry point (starts FastAPI server).
  - `lifecycle.py` handles agent orchestration.
  - `api.py` contains common API utility functions.

- **auth/** – Handles authentication and authorization:
  - Azure AD integration (verify tokens, manage roles, tenants).
  
- **config/** – Configuration management:
  - Environment variable management.
  - LangGraph and LangSmith specific settings.
  
- **graphs/** – Graphs orchestrating agents:
  - State management (`state/`).
  - Subgraphs for modular workflows (`subgraphs/`).

- **guardrails/** – Safety and compliance logic:
  - Input, execution, and output guards for agent actions.

- **nodes/** – Individual units of logic:
  - **Reasoning nodes** (planner, executor, critic)
  - **Control nodes** (guardrails, human review)
  - **Memory nodes** (update, store, retrieve)

- **prompts/** – Centralized prompt library:
  - Shared prompts, node prompts, agent-specific prompts, and templates.

- **services/** – Orchestration and utility services:
  - e.g., compliance service, audit service, evaluation service.

- **tools/** – Tool adapters and utilities for external interactions:
  - HTTP, Database, Queue adapters, LLM interfaces.

- **policies/** – Governance and policy definitions:
  - Agent policies, tool policies, data policies.

- **observability/** – Monitoring and logging:
  - LangSmith integration, tracing, metrics, logging.

---

## Key Notes

1. **Entry point:** `app/main.py`  
2. **FastAPI integration:** API routes and dependencies are defined under `api/` and included in `main.py`.  
3. **Azure AD auth:** All API routes can be protected using `auth/azure_ad.py`.  
4. **Agents:** Each agent can have its **own prompts and graph**, allowing modular orchestration.  
5. **Extensibility:**  
   - Add new agents under `agents/`  
   - Add new nodes under `nodes/`  
   - Add new services under `services/`  
   - Add new API endpoints under `api/v1/`  

This folder represents the **entire service logic** and is intended to be production-ready.

---

## How to Run

```bash
# Install dependencies
poetry install

# Start backend service
uvicorn app.main:app --host 0.0.0.0 --port 8000

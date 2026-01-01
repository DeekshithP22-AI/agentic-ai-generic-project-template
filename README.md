# Agentic AI Generic Project Template

This repository is a **production-grade, extensible template** for building **Agentic AI systems** using **LangGraph**, **LangSmith**, and modern backend engineering practices.

## Design Goals

- Support **single-service** and **multi-service monorepo** architectures
- Enable **complex agent workflows** (multi-agent, hierarchical, recursive)
- Be **production-ready** from day one
- Clean separation of:
  - API
  - Agents
  - Graphs
  - Nodes
  - Prompts
  - Tools
  - Guardrails
  - Policies
  - Observability
- Compatible with:
  - LangGraph API
  - LangSmith
  - FastMCP (as a separate service)
  - CI/CD and Infrastructure-as-Code

## Repo Structure Overview

- `app/` – All deployable services (backend, frontend, fastmcp, etc.)
- `docker/` – Container definitions
- `infra/` – Terraform / Cloud / CI-CD infrastructure
- `docs/` – Architecture and documentation
- `.env.example` – Canonical environment variable template
- `pyproject.toml` – Repo-wide Python tooling

This repo can be used as:
- A **single backend service**
- A **monorepo with multiple independently deployed services**

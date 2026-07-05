# CISO Copilot Agent

[![CI](https://github.com/kogunlowo123/ciso-copilot-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ciso-copilot-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Executive | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

CISO copilot agent that monitors security posture, tracks compliance status, assesses cyber risk, manages security program metrics, and provides security investment recommendations.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `assess_security_posture` | Assess overall security posture with maturity scoring |
| `track_compliance` | Track security compliance status across frameworks |
| `assess_cyber_risk` | Assess cyber risk using quantitative risk methodology |
| `monitor_security_metrics` | Monitor key security program metrics (MTTD, MTTR, incidents) |
| `generate_board_report` | Generate security board report for executive audience |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/ciso-copilot/synthesize` | Synthesize data |
| `POST` | `/api/v1/ciso-copilot/analyze` | Analyze |
| `GET` | `/api/v1/ciso-copilot/track` | Track metrics |
| `POST` | `/api/v1/ciso-copilot/recommend` | Get recommendation |
| `POST` | `/api/v1/ciso-copilot/report` | Generate report |

## Features

- Ciso
- Copilot
- Strategic Insights
- Decision Support

## Integrations

- Snowflake
- Tableau
- Salesforce
- Workday
- Jira

## Architecture

```
ciso-copilot-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ciso_copilot_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Enterprise Data Platform + LLM + BI**

---

Built as part of the Enterprise AI Agent Platform.

# EnterpriseAI-Support — Multi-Agent Customer Support System

**One-line:** A multi-agent system that automates tier-1 support and assists tier-2 via specialist subagents, memory, tools, and observability.

## Overview
This project demonstrates a production-minded multi-agent customer support system with:
- Root orchestrator + specialist agents (Billing, Diagnostics)
- Tools: KB lookup, Search (stub), Ticket API (stub), Diagnostics Executor
- Sessions & long-term memory (simulated vector store)
- Observability (logs, traces, metrics)
- Evaluation (LLM-as-Judge + manual HITL)
- Optional steps to deploy to Vertex AI Agent Engine

## How to run (Kaggle)
1. Create a new Kaggle Notebook and set runtime to Python 3.
2. Copy the notebook cells from `notebooks/agent_capstone.ipynb` (or paste the provided cell blocks).
3. Run cells in order. No external API keys are required for the demo (stubs simulate external tools).
4. To use Gemini or real search, add your API key and update tool wrappers (see below).

## Files of interest
- `notebooks/agent_capstone.ipynb` — demo notebook with code & markdown
- `src/` — source modules (agents, orchestrator, tools, memory, eval)
- `architecture/diagram.mmd` — Mermaid architecture diagram
- `video_script.txt` — demo video script

## Deployment (optional)
See `DEPLOYMENT.md` for step-by-step Vertex AI Agent Engine deployment instructions (manual steps requiring GCP project & billing).

## License
MIT

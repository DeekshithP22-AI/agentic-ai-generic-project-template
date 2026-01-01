Perfect! Let’s do the **`prompts/`** folder next. This is a **critical folder** for an agentic AI platform because it stores all prompt templates, system instructions, safety instructions, and agent-specific prompts. Proper organization here ensures **reusable, auditable, and modular prompts** for multiple agents and nodes.

Here’s a comprehensive **README.md** for `prompts/`:

---

# `prompts/` Folder README.md (Detailed Version)

```markdown
# Prompts Folder

## Overview

The `prompts/` folder contains all **prompt assets** used across the agentic AI platform. These are the **instructions, templates, and contextual prompts** that agents, nodes, and workflows use to generate responses, make decisions, and interact with tools.  

Organizing prompts properly is critical for:

- Multi-agent orchestration  
- Reusability across nodes and agents  
- Maintaining safety, consistency, and style  
- Easy auditing of LLM behavior  

---

## Folder Structure

```

prompts/
├── **init**.py
├── README.md
├── nodes/
│   ├── **init**.py
│   ├── planner.md
│   ├── executor.md
│   ├── critic.md
│   ├── summarizer.md
│   └── README.md
├── shared/
│   ├── **init**.py
│   ├── system.md
│   ├── style.md
│   ├── safety.md
│   └── README.md
├── templates/
│   ├── **init**.py
│   ├── reasoning.jinja
│   ├── tool_call.jinja
│   ├── response.jinja
│   └── README.md
├── agents/
│   ├── agent_one/
│   │   ├── **init**.py
│   │   ├── system.md
│   │   ├── goals.md
│   │   ├── constraints.md
│   │   └── README.md
│   └── agent_two/
│       ├── **init**.py
│       ├── system.md
│       ├── goals.md
│       └── README.md
├── compliance_prompt.py
├── risk_prompt.py
├── summary_prompt.py

````

---

## Purpose of Each Subfolder

### `nodes/`
- Prompts specific to **nodes** (planner, executor, critic, summarizer)  
- Node prompts define **how each node should reason, make decisions, or process data**  
- Example: `planner.md` may define step-by-step planning instructions for the planner node  

### `shared/`
- **Global/shared prompts** used across agents and nodes  
- Examples include:
  - `system.md` → overarching instructions for LLMs  
  - `style.md` → tone, formatting, or communication style  
  - `safety.md` → constraints to ensure safe outputs  

### `templates/`
- **Jinja-style templates** for dynamic prompt rendering  
- Common templates:
  - `reasoning.jinja` → reasoning steps to guide LLM logic  
  - `tool_call.jinja` → template for calling tools/apis  
  - `response.jinja` → response formatting template  

### `agents/`
- Each agent has its own folder with **agent-specific prompts**  
- Examples:
  - `system.md` → agent’s role and system instructions  
  - `goals.md` → high-level goals for the agent  
  - `constraints.md` → safety and policy constraints specific to that agent  
- Supports **multiple agents** in the system  

### `compliance_prompt.py`, `risk_prompt.py`, `summary_prompt.py`
- Python modules that **combine prompts dynamically** or provide **predefined prompt templates** for specific workflows  
- Example: `compliance_prompt.py` could fetch node prompts, shared prompts, and agent goals to generate the final prompt used for execution  

---

## Best Practices

1. **Modularization**
   - Keep **agent-specific prompts separate** from shared prompts  
   - Keep **node-specific prompts** modular so nodes can be reused across agents  

2. **Versioning**
   - Track changes to prompts for **auditability**  
   - Consider storing prompts in a **Git-managed folder**  

3. **Templates**
   - Use templates to dynamically insert context, variables, or workflow outputs  
   - Ensures **scalability and consistency**  

4. **Safety & Style**
   - Shared prompts (`safety.md`, `style.md`) enforce **guardrails and formatting consistency** across all agents and nodes  

5. **Dynamic Loading**
   - Prompts can be dynamically loaded at runtime based on:
     - Agent  
     - Node  
     - Workflow context  

---

## Integration With Other Folders

- **agents/** → Each agent folder in `agents/` can load its own prompts  
- **nodes/** → Node classes will reference `nodes/` prompts  
- **services/** → Service orchestrators fetch prompts to generate execution instructions for agents  
- **guardrails/** → Safety-related prompts are cross-checked with guardrail policies  

---

## Example: Loading a Node Prompt in Python

```python
from pathlib import Path

def load_prompt(node_name: str) -> str:
    prompt_path = Path(__file__).parent / "nodes" / f"{node_name}.md"
    with open(prompt_path) as f:
        return f.read()

planner_prompt = load_prompt("planner")
print(planner_prompt)
````

This ensures **dynamic and modular prompt loading**, supporting multi-agent workflows.

---

## Summary

The `prompts/` folder is **the heart of the LLM orchestration layer**:

* Supports **multiple agents**
* Provides **shared system, style, and safety instructions**
* Houses **node-specific reasoning instructions**
* Contains **dynamic templates** for generating context-aware prompts
* Fully integrated with **services, agents, nodes, and guardrails**
* Crucial for **reusable, auditable, and production-ready workflows**



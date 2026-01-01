import os

# ==========================
# Config
# ==========================
REPO_NAME = "agentic-ai-generic-project-template"
SERVICES = ["backend"]  # Add more services like "frontend", "fastmcp" if needed

ROOT_FILES = [
    ".env.example",
    "pyproject.toml"
]

ROOT_DIRS = ["docker", "docs", "infra", "guards", "app"]

# Docker placeholder files
DOCKER_FILES = ["docker/backend.Dockerfile"]

# Full service structure
SERVICE_STRUCTURE = {
    "src": [
        ".env",  # Optional service-level env
        "pyproject.toml",  # Optional service-level pyproject
        "langgraph.json",
        ("app", ["main.py", "api.py", "lifecycle.py"]),
        ("api", [("v1", ["router.py", "agents.py", "runs.py", "workflows.py", "health.py"]), "deps.py"]),
        ("agents", [
            ("agent_one", ["graph.py", "config.py", ("prompts", ["system.md", "goals.md", "constraints.md"])]),
            ("agent_two", ["graph.py", "config.py", ("prompts", ["system.md", "goals.md"])])
        ]),
        ("graphs", [("state", ["base.py", "shared.py"]), ("subgraphs", ["planning.py", "execution.py", "verification.py"])]),
        ("nodes", [
            "base.py",
            ("reasoning", ["planner.py", "executor.py", "critic.py"]),
            ("control", ["guardrail.py", "human_review.py"]),
            ("memory", ["updater.py"])
        ]),
        "services",
        ("tools", ["base.py", "registry.py", ("adapters", ["http.py", "database.py", "queue.py"])]),
        ("prompts", [
            ("shared", ["system.md", "style.md", "safety.md"]),
            ("nodes", ["planner.md", "executor.md", "critic.md", "summarizer.md"]),
            ("templates", ["reasoning.jinja", "tool_call.jinja", "response.jinja"])
        ]),
        "policies",
        "guardrails",
        "observability",
        "config",
        "auth"
    ]
}

README_CONTENT = "# {folder}\n\nThis folder contains: {description}\n"

# ==========================
# Helper functions
# ==========================
def create_file(path, content=""):
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(content)

def create_folder(path):
    os.makedirs(path, exist_ok=True)
    # Add __init__.py for Python packages
    if not path.endswith(("docs", "infra", "docker", "guards")):
        init_path = os.path.join(path, "__init__.py")
        create_file(init_path)
    # Add README.md
    readme_path = os.path.join(path, "README.md")
    create_file(readme_path, README_CONTENT.format(folder=path, description="Folder description"))

def process_structure(base_path, structure):
    for item in structure:
        if isinstance(item, str):
            # file or folder
            path = os.path.join(base_path, item)
            if item.endswith((".py", ".md", ".json", ".toml", ".env", ".jinja")):
                create_file(path, f"# {item} placeholder")
            else:
                create_folder(path)
        elif isinstance(item, tuple):
            folder_name, subitems = item
            folder_path = os.path.join(base_path, folder_name)
            create_folder(folder_path)
            process_structure(folder_path, subitems)

# ==========================
# Create root-level files and folders
# ==========================
for f in ROOT_FILES:
    create_file(f, f"# {f} - root-level file")

for d in ROOT_DIRS:
    create_folder(d)

# Docker placeholder files
for f in DOCKER_FILES:
    create_file(f, "# Dockerfile placeholder")

# ==========================
# Create services structure
# ==========================
for service in SERVICES:
    service_root = os.path.join("app", service, "src")
    create_folder(service_root)
    process_structure(service_root, SERVICE_STRUCTURE["src"])

print("✅ Project structure created successfully!")

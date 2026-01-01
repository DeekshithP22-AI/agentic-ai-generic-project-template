from langsmith import traceable

@traceable
def trace_step(name: str):
    return name

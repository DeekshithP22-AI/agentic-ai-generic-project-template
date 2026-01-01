def route_by_confidence(state: dict) -> str:
    if state.get("confidence", 0) > 0.8:
        return "accept"
    return "review"

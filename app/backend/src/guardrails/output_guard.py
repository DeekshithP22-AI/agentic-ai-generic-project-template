def validate_output(text: str):
    if "secret" in text.lower():
        raise ValueError("Sensitive data detected")

def classify_severity(reason):
    reason = reason.lower()

    if "or '1'='1" in reason:
        return "HIGH"

    if "<script>" in reason:
        return "HIGH"

    if "/admin" in reason or "/login" in reason:
        return "MEDIUM"

    return "LOW"

SUSPICIOUS_PATTERNS = [
    "/admin",
    "/login",
    "or '1'='1",
    "<script>"
]

def analyze_logs(log_file_path):
    incidents = []

    with open(log_file_path, "r") as file:
        for line in file:
            for pattern in SUSPICIOUS_PATTERNS:
                if pattern.lower() in line.lower():
                    incidents.append({
                        "log": line.strip(),
                        "reason": f"Suspicious pattern detected: {pattern}"
                    })
                    break  # stop checking other patterns for this line

    return incidents

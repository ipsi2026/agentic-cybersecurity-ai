def extract_ip(log_line):
    return log_line.split()[0]

def analyze_ip_behavior(reports):
    ip_activity = {}

    for report in reports:
        ip = extract_ip(report["log"])
        ip_activity[ip] = ip_activity.get(ip, 0) + 1

    return ip_activity

def escalate_severity_if_needed(report, ip_activity, threshold=2):
    ip = extract_ip(report["log"])

    if ip_activity.get(ip, 0) >= threshold and report["severity"] == "MEDIUM":
        report["severity"] = "HIGH"
        report["recommended_action"] = "Repeated suspicious activity detected – block IP"

    return report

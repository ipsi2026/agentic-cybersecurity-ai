from datetime import datetime

def generate_report(incident, severity):
    report = {
        "timestamp": datetime.now().isoformat(),
        "severity": severity,
        "reason": incident["reason"],
        "log": incident["log"],
        "recommended_action": recommend_action(severity)
    }
    return report

def recommend_action(severity):
    if severity == "HIGH":
        return "Immediate investigation and block source IP"
    elif severity == "MEDIUM":
        return "Monitor activity and alert administrator"
    else:
        return "Log for review"

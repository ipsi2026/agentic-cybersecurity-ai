from agent.log_monitor import analyze_logs
from agent.agent.severity_classifier import classify_severity

def main():
    incidents = analyze_logs("logs/logs/access.log")

    if not incidents:
        print("✅ No suspicious activity detected.")
        return

    print("🚨 Suspicious activity detected:\n")

    for idx, incident in enumerate(incidents, 1):
        severity = classify_severity(incident["reason"])

        print(f"{idx}. Severity: {severity}")
        print(f"   Reason: {incident['reason']}")
        print(f"   Log: {incident['log']}\n")

if __name__ == "__main__":
    main()

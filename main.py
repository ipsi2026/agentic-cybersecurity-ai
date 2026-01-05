from agent.log_monitor import analyze_logs
from agent.severity_classifier import classify_severity
from agent.agent.reporter import generate_report
import json

def main():
    incidents = analyze_logs("logs/logs/access.log")

    if not incidents:
        print("✅ No suspicious activity detected.")
        return

    all_reports = []

    print("🚨 Suspicious activity detected:\n")

    for idx, incident in enumerate(incidents, 1):
        severity = classify_severity(incident["reason"])
        report = generate_report(incident, severity)
        all_reports.append(report)

        print(f"{idx}. Severity: {severity}")
        print(f"   Reason: {incident['reason']}")
        print(f"   Action: {report['recommended_action']}\n")

    with open("memory/incidents.json", "w") as file:
        json.dump(all_reports, file, indent=4)

    print("📄 Incident reports saved to memory/incidents.json")

if __name__ == "__main__":
    main()

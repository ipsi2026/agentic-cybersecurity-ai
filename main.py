from agent.log_monitor import analyze_logs
from agent.severity_classifier import classify_severity
from agent.agent.reporter import generate_report
from agent.agent.ip_analyzer import analyze_ip_behavior, escalate_severity_if_needed
import json

def main():
    incidents = analyze_logs("logs/logs/access.log")

    if not incidents:
        print(" No suspicious activity detected.")
        return

    initial_reports = []

    for incident in incidents:
        severity = classify_severity(incident["reason"])
        report = generate_report(incident, severity)
        initial_reports.append(report)

    ip_activity = analyze_ip_behavior(initial_reports)

    final_reports = []
    print(" Suspicious activity detected:\n")

    for idx, report in enumerate(initial_reports, 1):
        report = escalate_severity_if_needed(report, ip_activity)
        final_reports.append(report)

        print(f"{idx}. Severity: {report['severity']}")
        print(f"   Reason: {report['reason']}")
        print(f"   Action: {report['recommended_action']}\n")

    with open("memory/incidents.json", "w") as file:
        json.dump(final_reports, file, indent=4)

    print(" Incident reports updated with IP behavior analysis")

if __name__ == "__main__":
    main()

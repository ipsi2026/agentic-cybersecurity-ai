from agent.log_monitor import analyze_logs
from agent.severity_classifier import classify_severity
from agent.reporter import generate_report
from agent.ip_analyzer import analyze_ip_behavior, escalate_severity_if_needed
from tools.tools.ip_blocker import block_ip
from tools.tools.alert_system import send_alert

def extract_ip(log_line):
    return log_line.split()[0]

def run_agent(log_path):
    incidents = analyze_logs(log_path)

    if not incidents:
        return []

    initial_reports = []

    for incident in incidents:
        severity = classify_severity(incident["reason"])
        report = generate_report(incident, severity)
        initial_reports.append(report)

    ip_activity = analyze_ip_behavior(initial_reports)

    final_reports = []

    for report in initial_reports:
        report = escalate_severity_if_needed(report, ip_activity)
        ip = extract_ip(report["log"])

        if report["severity"] == "HIGH":
            report["action_taken"] = block_ip(ip)
            send_alert(report)
        elif report["severity"] == "MEDIUM":
            send_alert(report)
            report["action_taken"] = "Alert sent"
        else:
            report["action_taken"] = "Logged only"

        final_reports.append(report)

    return final_reports

def send_alert(report):
    print(f"📢 ALERT: {report['severity']} threat detected")
    print(f"    Reason: {report['reason']}")
    print(f"    Recommended Action: {report['recommended_action']}")

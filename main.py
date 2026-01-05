from agent.log_monitor import analyze_logs

def main():
    incidents = analyze_logs("logs/logs/access.log")

    if not incidents:
        print("✅ No suspicious activity detected.")
    else:
        print("🚨 Suspicious activity detected:\n")
        for idx, incident in enumerate(incidents, 1):
            print(f"{idx}. {incident['reason']}")
            print(f"   Log: {incident['log']}\n")

if __name__ == "__main__":
    main()

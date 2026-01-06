from agent.orchestrator import run_agent
import json

def main():
    print(" Agentic AI Cybersecurity System Running...\n")

    reports = run_agent("logs/logs/access.log")

    if not reports:
        print(" No suspicious activity detected.")
        return

    with open("memory/incidents.json", "w") as file:
        json.dump(reports, file, indent=4)

    print(" Final incident reports saved to memory/incidents.json")

if __name__ == "__main__":
    main()

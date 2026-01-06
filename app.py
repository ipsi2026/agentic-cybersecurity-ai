import streamlit as st
import json
from agent.orchestrator import run_agent

st.set_page_config(
    page_title="Agentic AI Cybersecurity Dashboard",
    layout="wide"
)

st.title(" Agentic AI Cybersecurity Monitoring System")

st.markdown("""
This dashboard runs an **autonomous security agent** that:
- Monitors web server logs  
- Detects malicious activity  
- Classifies severity  
- Takes automated actions  
""")

if st.button(" Run Security Agent"):
    with st.spinner("Analyzing logs and detecting threats..."):
        reports = run_agent("logs/logs/access.log")

        if not reports:
            st.success(" No suspicious activity detected.")
        else:
            with open("memory/incidents.json", "w") as file:
                json.dump(reports, file, indent=4)

            st.error(f" {len(reports)} suspicious incidents detected!")

            st.subheader(" Incident Reports")

            for report in reports:
                if report["severity"] == "HIGH":
                    st.markdown(
                        f"**HIGH** | {report['reason']}  \n"
                        f"**Action:** {report['action_taken']}"
                    )
                elif report["severity"] == "MEDIUM":
                    st.markdown(
                        f" **MEDIUM** | {report['reason']}  \n"
                        f"**Action:** {report['action_taken']}"
                    )
                else:
                    st.markdown(
                        f" **LOW** | {report['reason']}  \n"
                        f"**Action:** {report['action_taken']}"
                    )

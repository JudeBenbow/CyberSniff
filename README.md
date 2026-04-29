# 🛡️ CyberSniff: Real-Time Network Traffic Analyzer

A professional-grade Network Packet Sniffer and Visualization dashboard built for cybersecurity telemetry and traffic analysis. This tool captures live network data, parses protocols at the IP layer, and provides an interactive web-based dashboard for monitoring network health and anomalies.

## 🚀 Key Features
* **Live Packet Capture:** Real-time sniffing of IP-based traffic using Scapy.
* **Protocol Telemetry:** Dynamic breakdown of TCP, UDP, and ICMP traffic.
* **Interactive Dashboard:** Built with Streamlit and Plotly for visual data analysis.
* **Traffic Filtering:** Sidebar controls to isolate specific protocols for deep-dive analysis.
* **Data Persistence:** Automated logging to CSV for historical audit trails.
* **Bandwidth Monitoring:** Real-time calculation of data throughput in Megabytes (MB).

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Packet Processing:** Scapy
* **Data Analytics:** Pandas
* **Visualization:** Plotly & Streamlit
* **Driver:** Npcap (Windows) / Libpcap (Linux)

## 📸 Dashboard Preview
*(Tip: Take a screenshot of your working dashboard and put it here!)*

## 🚦 Installation & Setup

1. **Prerequisites:**
   * Install [Npcap](https://npcap.com/) (Ensure "WinPcap API-compatible Mode" is checked).
   * Python 3.10+ installed.

2. **Clone the Repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/CyberSniff.git](https://github.com/YOUR_USERNAME/CyberSniff.git)
   cd CyberSniff
Set Up Virtual Environment:

Bash
python -m venv venv
.\venv\Scripts\activate
pip install scapy pandas streamlit plotly
🖥️ Usage
Start the Capture Engine:
Run the sniffer as Administrator to allow promiscuous mode access.

PowerShell
python sniffer.py
Launch the Analytics Dashboard:
In a separate terminal:

PowerShell
streamlit run visualizer.py
⚖️ Disclaimer
This tool is for educational and authorized security testing purposes only. Sniffing network traffic on networks you do not own or have explicit permission to test is illegal and unethical. Use responsibly.

# <p align="center">🐍 NETVIPER</p>
<p align="center"><b>ADVANCED NETWORK PACKET ANALYZER</b></p>

> Professional-grade real-time packet analyzer built for cybersecurity research, traffic monitoring, and educational auditing.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Network%20Analysis-green?style=for-the-badge)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-black?style=for-the-badge)

---

## 📌 Overview

**NetViper** is a professional real-time network packet analyzer designed for cybersecurity students and practitioners. The tool provides a modern interface capable of capturing and analyzing live network traffic with forensic-level visibility.

Built using **Python**, **Scapy**, and **CustomTkinter**, NetViper ensures all captured traffic remains local to the host machine, making it suitable for secure auditing and cybersecurity learning environments.

---

## ✨ Features

- 🔍 **Real-Time Packet Sniffing**: Live traffic capture directly from network interfaces.
- 🌐 **Multi-Protocol Analysis**: Supports IP, TCP, UDP, and ICMP.
- 📝 **Session Export**: Export captured sessions into forensic `.txt` logs.
- 🎨 **Modern Cyberpunk UI**: Dark carbon interface with high-contrast console output.
- 🔒 **Local Data Processing**: No cloud storage; all data stays on your machine.

---

## 🖥️ Interface Preview

```text
┌────────────────────────────────────┐
│         NetViper Console           │
├────────────────────────────────────┤
│ 149.88.23.102 -> 172.20.10.2 | Proto: 17
│ 172.20.10.2 -> 149.88.23.102 | Proto: 17
│ Status: Monitoring Live Traffic... │
└────────────────────────────────────┘
```

---

# ⚙️ Installation

## Windows Setup

### 1️⃣ Install Npcap

Download and install Npcap:

👉 https://npcap.com/

> أثناء التثبيت قم بتفعيل:
> **"WinPcap API-compatible Mode"**

---

### 2️⃣ Install Python Dependencies

```bash
pip install customtkinter scapy
```

---

### 3️⃣ Run NetViper

Open terminal as **Administrator** and execute:

```bash
python netviper.py
```

---

# 🐧 Linux Setup

## Install Dependencies

```bash
sudo apt install python3-pip
pip3 install customtkinter scapy
```

---

## Run with Root Privileges

```bash
sudo python3 netviper.py
```

---

# 🧠 Technical Workflow

| ID | Phase | Functionality |
|----|--------|----------------|
| 01 | INIT | Initializes threaded Scapy sniffing engine |
| 02 | CAPTURE | Hooks raw sockets for incoming/outgoing frames |
| 03 | DISSECT | Extracts IP addresses and protocol information |
| 04 | OUTPUT | Sanitizes payloads and streams to live UI |
| 05 | COMMIT | Saves captured session data to forensic logs |



# 📋 Requirements

- Python 3.x
- Scapy
- CustomTkinter
- Npcap (Windows only)
- Root/Admin privileges

---

# 🔐 Ethical Use Disclaimer

> Unauthorized monitoring or interception of network traffic is illegal.

NetViper is intended strictly for:

- Educational purposes
- Authorized penetration testing
- Security auditing
- Internship research environments

Always obtain proper authorization before monitoring any network traffic.


# 👨‍💻 Developed By

**Mohammed Shezil**  
Prodigy InfoTech — Secure Core v1.2

---

# 🔗 Repository

[GitHub Repository](https://github.com/Mohammedshezil/PRODIGY-CS-05)

---

# ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork the project
- 🛡️ Contribute improvements
- 📢 Share with the cybersecurity community

---

# 📜 License

This project is intended for educational and research purposes only.

Use responsibly.

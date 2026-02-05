# 🔐 Laptop Login Alert System (Silent & Secure)

A lightweight, invisible Python automation tool that instantly notifies you via Telegram whenever your laptop is turned on. Designed for security and peace of mind, it provides critical details like location (IP) and power status without alerting any unauthorized users.

## 🚀 Features

* **⚡ Instant Notification:** Sends an alert the moment an internet connection is established.
* **🌍 Location Tracking:** Captures the **Public IP Address** to help locate the device if stolen.
* **🔋 Power Status:** Detects if the laptop is running on **Battery** or **Plugged In**.
* **👻 Stealth Mode:** Runs silently in the background with no pop-up windows or visible interface.
* **🛡️ Secure Whitelist:** Uses a "Chat ID" lock so only **YOU** can receive data (ignores strangers).
* **🔄 Auto-Kill:** The script automatically terminates itself after sending the message to save resources.

---

## 🛠️ Prerequisites

You need **Python** installed on your Windows machine.

### Required Libraries
Open your terminal (Command Prompt) and install the necessary dependencies:

```bash
pip install requests psutil

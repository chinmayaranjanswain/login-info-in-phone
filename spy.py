import requests
import time
import socket
import psutil
from datetime import datetime

# --- 🔒 SECURITY CONFIGURATION ---
# Replace these with your actual details
# token = "8529630607:AAFoYwbpzA4hmm0juTQUR0I0wy5w3L6w_4g"
# chat_id = "6154899005"
BOT_TOKEN = "8529630607:AAFoYwbpzA4hmm0juTQUR0I0wy5w3L6w_4g"
OWNER_ID = "6154899005"  # <--- This is the Key. Only this ID gets messages.
# ---------------------------------

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except:
        return "Unavailable"

def get_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            return "🖥️ Desktop PC (AC Power)"
        
        plugged = "🔌 Plugged In" if battery.power_plugged else "🔋 On Battery"
        return f"{plugged} ({battery.percent}%)"
    except:
        return "Unknown"

def send_secure_alert():
    # 1. Gather Data
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = get_public_ip()
    power = get_battery_status()

    # 2. Format Message
    message = (
        f"🔐 ** LOGIN ALERT**\n"
        f"\n"
        f"👤 **Device:\n ** `{hostname}`\n \n"
        f"🕒 **Time:\n ** {current_time}\n \n"
        f"🌍 **IP Address:\n ** `{ip}`\n \n"
        f"⚡ **Power:\n ** {power}\n \n"
        f"\n------------------------"
    )

    # 3. Send ONLY to the Owner ID
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": OWNER_ID, # <--- This ensures data goes ONLY to you
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        requests.post(url, data=data)
        print("✅ Secure alert sent to owner.")
    except Exception as e:
        print(f"❌ Failed to send: {e}")

def wait_for_internet_connection():
    print("⏳ Waiting for internet...")
    while True:
        try:
            # Try to ping Google's DNS server to check connectivity
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            print("✅ Internet Connected!")
            return True
        except OSError:
            pass
        time.sleep(5) # Wait 5 seconds before retrying

if __name__ == "__main__":
    # Step 1: Wait for Wi-Fi
    wait_for_internet_connection()
    
    # Step 2: Allow system to settle (optional 2s pause)
    time.sleep(2)
    
    # Step 3: Send the Alert
    send_secure_alert()
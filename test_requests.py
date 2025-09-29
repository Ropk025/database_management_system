import requests

try:
    response = requests.get("http://127.0.0.1:8000/")
    print("✅ Server response:", response.text)
except requests.exceptions.RequestException as e:
    print("❌ Connection failed:", e)
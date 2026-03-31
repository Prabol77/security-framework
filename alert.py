# alert.py

def raise_alert(message):
    print("\n🚨 ALERT:", message)

    if "Buffer Overflow" in message:
        print("👉 Suggestion: Limit input size")

    elif "Suspicious Process" in message:
        print("👉 Suggestion: Terminate process")
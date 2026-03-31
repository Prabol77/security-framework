# detector.py

def detect_vulnerability(event):
    if event["type"] == "buffer_overflow":
        if len(event["data"]) > 5000:
            return "Buffer Overflow Detected"

    elif event["type"] == "suspicious_process":
        if "malware" in event["process"]:
            return "Suspicious Process Detected"

    return None
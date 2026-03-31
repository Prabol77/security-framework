# simulator.py
# Simulation module added
def buffer_overflow_simulation():
    data = "A" * 10000
    return {"type": "buffer_overflow", "data": data}


def fake_process_simulation():
    return {"type": "suspicious_process", "process": "malware.exe"}
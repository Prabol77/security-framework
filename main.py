# main.py

from simulator import buffer_overflow_simulation, fake_process_simulation
from detector import detect_vulnerability
from alert import raise_alert
from logger import log_event


def run_system():
    print("🔐 Security Vulnerability Detection Framework Running...\n")

    events = [
        buffer_overflow_simulation(),
        fake_process_simulation()
    ]

    for event in events:
        result = detect_vulnerability(event)

        if result:
            raise_alert(result)
            log_event(result)


if __name__ == "__main__":
    run_system()
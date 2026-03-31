# gui.py
# GUI interface added
import tkinter as tk
from simulator import buffer_overflow_simulation, fake_process_simulation
from detector import detect_vulnerability


def run_simulation():
    output.delete(1.0, tk.END)

    events = [
        buffer_overflow_simulation(),
        fake_process_simulation()
    ]

    for event in events:
        result = detect_vulnerability(event)

        if result:
            output.insert(tk.END, f"🚨 {result}\n")

            if "Buffer Overflow" in result:
                output.insert(tk.END, "👉 Suggestion: Limit input size\n\n")

            elif "Suspicious Process" in result:
                output.insert(tk.END, "👉 Suggestion: Terminate process\n\n")


# GUI Window
root = tk.Tk()
root.title("Security Vulnerability Detector")
root.geometry("500x400")

title = tk.Label(root, text="Security Vulnerability Detection System", font=("Arial", 14))
title.pack(pady=10)

run_btn = tk.Button(root, text="Run Simulation", command=run_simulation)
run_btn.pack(pady=10)

output = tk.Text(root, height=15, width=60)
output.pack(pady=10)

root.mainloop()
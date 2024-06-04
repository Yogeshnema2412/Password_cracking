import tkinter as tk
from tkinter import ttk, messagebox
import itertools
import string
import time

# Function to attempt password cracking
def brute_force_crack(target, charset, max_length):
    total_attempts = sum(len(charset) ** i for i in range(1, max_length + 1))
    attempt_count = 0

    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            attempt_count += 1
            yield attempt, attempt_count / total_attempts
            if attempt == target:
                return attempt

# Function to start the brute force cracking process
def start_cracking():
    target_password = entry_target.get()
    max_length = int(entry_length.get())
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    progress_label.config(text="Starting brute force cracking...")
    result = None
    start_time = time.time()

    for attempt, progress in brute_force_crack(target_password, charset, max_length):
        progress_label.config(text=f"Trying: {attempt}")
        progress_bar['value'] = progress * 100
        root.update()
        if attempt == target_password:
            result = attempt
            break

    end_time = time.time()
    if result:
        messagebox.showinfo("Success", f"Password cracked: {result}\nTime taken: {end_time - start_time:.2f} seconds")
    else:
        messagebox.showwarning("Failure", "Failed to crack the password within the given length")

# Setting up the GUI
root = tk.Tk()
root.title("Password Cracking - Brute Force")

# Styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TProgressbar", thickness=20)

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(main_frame, text="Target Password:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_target = ttk.Entry(main_frame, width=30)
entry_target.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)

ttk.Label(main_frame, text="Max Length:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_length = ttk.Entry(main_frame, width=30)
entry_length.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

start_button = ttk.Button(main_frame, text="Start Cracking", command=start_cracking)
start_button.grid(row=2, column=0, columnspan=2, pady=20)

progress_label = ttk.Label(main_frame, text="")
progress_label.grid(row=3, column=0, columnspan=2, pady=10)

progress_bar = ttk.Progressbar(main_frame, orient='horizontal', mode='determinate', length=400)
progress_bar.grid(row=4, column=0, columnspan=2, pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

root.mainloop()
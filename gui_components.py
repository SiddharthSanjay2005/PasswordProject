import tkinter as tk
from tkinter import ttk, messagebox
from password_utils import evaluate_password, generate_password

def create_gui(root):
    root.title("Password Strength Checker")
    root.geometry("480x340")
    root.resizable(False, False)

    pwd_var = tk.StringVar()
    show_var = tk.BooleanVar(value=False)

    heading = tk.Label(root, text="🔐 Password Strength Checker",
                       font=("Segoe UI", 14, "bold"))
    heading.pack(pady=(12, 6))

    frame = tk.Frame(root, padx=12, pady=6)
    frame.pack(fill='x')

    tk.Label(frame, text="Enter Password:", anchor='w').pack(fill='x')
    entry = tk.Entry(frame, textvariable=pwd_var, show='*',
                     font=("Segoe UI", 12))
    entry.pack(fill='x', pady=6)

    result_label = tk.Label(frame, text=" ", font=("Segoe UI", 12, "bold"))
    result_label.pack()

    # Gradient progress bar (simulated with style updates)
    style = ttk.Style()
    style.theme_use('default')
    style.configure("TProgressbar", thickness=20)

    progress = ttk.Progressbar(frame, length=420, maximum=100, mode='determinate')
    progress.pack(pady=10)

    suggestions_label = tk.Label(frame, text="", font=("Segoe UI", 10),
                                 fg="gray", justify='left')
    suggestions_label.pack()

    # --- Event Handlers ---
    def on_keyrelease(event=None):
        pwd = pwd_var.get()
        status, color, percent, suggestions = evaluate_password(pwd)
        result_label.config(text=status, fg=color)
        progress['value'] = percent

        # Gradient effect (manual simulation)
        if percent < 40:
            style.configure("TProgressbar", background="red")
        elif percent < 80:
            style.configure("TProgressbar", background="orange")
        else:
            style.configure("TProgressbar", background="green")

        # Show suggestions
        if suggestions:
            suggestions_label.config(
                text="Suggestions:\n- " + "\n- ".join(suggestions))
        else:
            suggestions_label.config(text="Looks great! ✅")

    def toggle_show():
        entry.config(show='' if show_var.get() else '*')

    def generate_new_password():
        new_pwd = generate_password(12, use_special=True)
        pwd_var.set(new_pwd)
        on_keyrelease()

    def copy_password():
        root.clipboard_clear()
        root.clipboard_append(pwd_var.get())
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    entry.bind('<KeyRelease>', on_keyrelease)
    tk.Checkbutton(frame, text="Show password", variable=show_var,
                   command=toggle_show).pack(anchor='w')

    # Buttons for generator and copy
    btn_frame = tk.Frame(frame)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Generate Password",
              command=generate_new_password, bg="blue", fg="white").pack(side="left", padx=5)

    tk.Button(btn_frame, text="Copy to Clipboard",
              command=copy_password, bg="green", fg="white").pack(side="left", padx=5)

    # Initial state
    on_keyrelease()
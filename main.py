import tkinter as tk
import re

# Function to check password strength
def check_password_strength(event=None):
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        label_result.config(text="Strong ", fg="green")
    elif score >= 3:
        label_result.config(text="Moderate ", fg="orange")
    else:
        label_result.config(text="Weak ", fg="red")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="#1e1e1e")

label_title = tk.Label(root, text="🔐 Password Strength Checker", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
label_title.pack(pady=20)

entry = tk.Entry(root, show="*", font=("Arial", 14), width=25, justify="center")
entry.pack(pady=10)
entry.bind("<KeyRelease>", check_password_strength)

label_result = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#1e1e1e")
label_result.pack(pady=20)

info_label = tk.Label(root, text="Use uppercase, lowercase, numbers & special symbols.",
                      font=("Arial", 10), fg="#aaaaaa", bg="#1e1e1e")
info_label.pack(pady=10)

root.mainloop()

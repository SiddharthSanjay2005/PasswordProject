import re
import random
import string

def evaluate_password(pwd: str):
    """Return (status_text, color, percent_strength, suggestions)."""
    length_ok = len(pwd) >= 8
    lower = bool(re.search(r'[a-z]', pwd))
    upper = bool(re.search(r'[A-Z]', pwd))
    digit = bool(re.search(r'\d', pwd))
    special = bool(re.search(r'[@$!%*?&#]', pwd))

    score = sum([length_ok, lower, upper, digit, special])  # 0–5
    suggestions = []

    if not length_ok:
        suggestions.append("Use at least 8 characters")
    if not lower:
        suggestions.append("Add a lowercase letter")
    if not upper:
        suggestions.append("Add an uppercase letter")
    if not digit:
        suggestions.append("Add a number")
    if not special:
        suggestions.append("Add a special character (@$!%*?&#)")

    if score == 5:
        status, color = "Strong Password ✅", "green"
    elif score >= 3:
        status, color = "Moderate Password ⚠️", "orange"
    else:
        status, color = "Weak Password ❌", "red"

    percent = int(score / 5 * 100)
    return status, color, percent, suggestions


def generate_password(length=12, use_special=True):
    """Generate a strong random password."""
    chars = string.ascii_letters + string.digits
    if use_special:
        chars += "@$!%*?&#"
    return ''.join(random.choice(chars) for _ in range(length))
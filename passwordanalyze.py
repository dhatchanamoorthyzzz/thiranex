# Password Strength Analyzer
# Developed by: [Your Name]
# Description: Evaluates the strength of user-entered passwords based on length, character variety, and common patterns.

import re

def analyze_password_strength(password):
    score = 0
    remarks = ""

    # Criteria checks
    if len(password) < 8:
        remarks = "Password too short! Minimum 8 characters required."
        score = 1
    else:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Common patterns
    common_patterns = ["password", "12345", "qwerty", "abc", "letmein"]
    if any(pattern in password.lower() for pattern in common_patterns):
        remarks = "Avoid common patterns like 'password' or '12345'."
        score -= 1

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return f"Strength: {strength}\nScore: {score}/5\nRemarks: {remarks}"

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    print(analyze_password_strength(user_password))

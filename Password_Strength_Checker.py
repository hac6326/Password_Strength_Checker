import re

def password_strength(password):
    strength = 0

    # Check password length
    if len(password) < 8:
        return "Weak"

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    # Categorize password strength
    if strength == 2:
        return "Weak"
    elif strength == 3:
        return "Medium"
    else:
        return "Strong"

def main():
    password = input("Enter a password: ")
    print("Password strength:", password_strength(password))

if __name__ == "__main__":
    main()
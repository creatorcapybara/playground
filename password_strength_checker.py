import re

def check_password_strength(password):
    length_ok = len(password) >= 8
    digit_ok = re.search(r"\d", password)
    upper_ok = re.search(r"[A-Z]", password)
    lower_ok = re.search(r"[a-z]", password)
    special_ok = re.search(r"[\W_]", password) # Non-alphanumeric

    if all([length_ok, digit_ok, upper_ok, lower_ok, special_ok]):
        return "Strong Password"
    else:
        return "Weak Password: Must be 8+ chars, with upper, lower, digit, and special char."

# Test the function
pwd = input("Enter a password to check: ")
print(check_password_strength(pwd))

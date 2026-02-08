
import string 
import secrets
def generate_strong_password(length=12):
    """
    Generates a strong, random password of a specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A randomly generated password.
    """
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars
    
    password = []
    password.append(secrets.choice(string.ascii_lowercase))
    password.append(secrets.choice(string.ascii_uppercase))
    password.append(secrets.choice(string.digits))
    password.append(secrets.choice(string.punctuation))
    
    for i in range(length - 4):
        password.append(secrets.choice(all_chars))
    
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

password_length = 16 
new_password = generate_strong_password(password_length)

print(f"Generated Password: {new_password}")

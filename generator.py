import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    """
    Generate a random password based on user preferences.
    """
    # Ensure minimum password length
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Base character pool
    char_pool = list(string.ascii_lowercase)

    # Add character types based on user preferences
    if use_upper:
        char_pool.extend(string.ascii_uppercase)
    if use_digits:
        char_pool.extend(string.digits)
    if use_special:
        char_pool.extend(string.punctuation)

    # Ensure the password includes at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle the password to randomize it
    random.shuffle(password)

    return ''.join(password)

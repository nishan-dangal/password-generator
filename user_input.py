def get_user_input():
    """
    Gather user preferences for the password generation.
    """
    print("Welcome to the Password Generator!")
    try:
        # Get password length
        length = int(input("Enter your password length (minimum 4): "))
    except ValueError:
        print("Invalid input by the user. Setting default length to 12.")
        length = 12

    # Get preferences for character types
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    return length, use_upper, use_digits, use_special

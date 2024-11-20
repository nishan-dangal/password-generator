from generator import generate_password
from user_input import get_user_input

def main():
    """
    Main function to run the Password Generator.
    """
    try:
        # Gather user preferences
        length, use_upper, use_digits, use_special = get_user_input()

        # Generate the password
        password = generate_password(length, use_upper, use_digits, use_special)

        # Display the generated password
        print("\nYour generated password is:")
        print(password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

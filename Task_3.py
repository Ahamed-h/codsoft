import random
import string


def generate_password():
    print("=== Password Generator ===")

    # Ask user for password length
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if length < 4:
        print("Password length should be at least 4 for strength.")
        return

    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    generate_password()

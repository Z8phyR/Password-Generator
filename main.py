import random
import string
from cryptography.fernet import Fernet


def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define the characters to use
    lowercase_letters = string.ascii_lowercase
    all_characters = lowercase_letters

    if use_uppercase:
        uppercase_letters = string.ascii_uppercase
        all_characters += uppercase_letters

    if use_digits:
        digits = string.digits
        all_characters += digits

    if use_special:
        special_characters = string.punctuation
        all_characters += special_characters

    # Initialize an empty password
    password = ""

    # Helper function to avoid two consecutive similar types of characters
    def different_type(c1, c2):
        return (c1.islower() and not c2.islower()) or \
               (c1.isupper() and not c2.isupper()) or \
               (c1.isdigit() and not c2.isdigit()) or \
               (c1 in string.punctuation and c2 not in string.punctuation)

    # Generate the remaining characters
    while len(password) < length:
        next_char = random.choice(all_characters)

        # Check conditions: unique consecutive characters and different types for consecutive characters
        if len(password) == 0 or (next_char != password[-1] and different_type(next_char, password[-1])):
            password += next_char

    return password


def get_integer_input(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"The value should be at least {minimum}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def evaluate_password_strength(password):
    score = 0

    # Length criteria
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character type criteria
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    return score


def display_strength(score):
    strength = "Unknown"
    emoji = ""

    if score <= 2:
        strength = "Weak"
        emoji = "😟"
    elif score == 3:
        strength = "Moderate"
        emoji = "😐"
    elif score == 4:
        strength = "Strong"
        emoji = "😃"
    elif score >= 5:
        strength = "Very Strong"
        emoji = "🥳"

    print(f"Password Strength: {strength} {emoji}")


def main():
    """
    This function generates random passwords based on user input and displays their strength.
    It also gives the option to encrypt the password using Fernet encryption.
    """
    length = get_integer_input("Enter the password length: ", minimum=6)

    use_uppercase = input(
        "Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input(
        "Include special characters? (yes/no): ").strip().lower() == 'yes'
    amount = get_integer_input("How many passwords to generate? ", minimum=1)
    encrypt_choice = input(
        "Do you want to encrypt the password? (yes/no): ").strip().lower() == 'yes'
    if encrypt_choice:
        hardcoded_key = b'Dd0Dii3zQAyDQ7oQsxWtKFoLAZhiuWh_gm2iYUfPaDk='
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        for _ in range(amount):
            password = generate_password(
                length, use_uppercase, use_digits, use_special)
            score = evaluate_password_strength(password)
            display_strength(score)
            encrypted_password = cipher_suite.encrypt(password.encode())
            print(f"Generated encrypted password:",
                  encrypted_password.decode('utf-8'))
        print()
        print(f"Encryption key:", key.decode('utf-8'))
    else:
        for _ in range(amount):
            password = generate_password(
                length, use_uppercase, use_digits, use_special)
            print(f"Generated password: {password}")
            score = evaluate_password_strength(password)
            display_strength(score)
            print()


if __name__ == '__main__':
    main()

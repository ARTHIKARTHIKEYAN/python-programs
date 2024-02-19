import random
import string

def generate_password(length, include_numbers=True, include_symbols=True):
    characters = string.ascii_letters  # Uppercase and lowercase letters

    if include_numbers:
        characters += string.digits  # Include numbers

    if include_symbols:
        characters += string.punctuation  # Include symbols

    if length < 1:
        print("Password length must be at least 1 character.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random Password Generator")

    # Get user input for password criteria
    length = int(input("Enter the desired length of the password: "))
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    # Generate and display the password
    generated_password = generate_password(length, include_numbers, include_symbols)

    if generated_password:
        print(f"\nGenerated Password: {generated_password}")
    else:
        print("Password generation failed.")

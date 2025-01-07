import random
import string

def password_generator():
    print("\n=== Password Generator ===")
    length = int(input("Enter the desired password length: "))
    include_special = input("Include special characters? (y/n): ").lower() == 'y'

    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")
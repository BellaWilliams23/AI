# Programmer: Bella Williams
# Date: 3.12.2024
# Program: PasswordGenerator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import secrets

def generate_salt():
    # Generate a random salt using secrets module
    return secrets.token_hex(16)

def hash_password(password, salt):
    # Combine password and salt, then hash using SHA-256
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed_password

try:
    # Get user input for password
    password = input("Enter your password: ")

    # Generate a random salt
    salt = generate_salt()

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password and salt
    print(f"Hashed Password: {hashed_password}")
    print(f"Salt: {salt}")

except Exception as e:
    print(f"An error occurred: {e}")

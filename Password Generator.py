import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 4 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    
    try:
        user_length = int(input("Enter desired password length (min 8): "))
        print("Generated password:", generate_password(user_length))
    except ValueError as e:
        print("Error:", e)
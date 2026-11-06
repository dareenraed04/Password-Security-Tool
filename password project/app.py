import string
import random

def check_password(password):
    score = 0
# Test review
    if len(password) >= 8:
        score += 30
    else:
        print("Password too short❌")

    if any(c.islower() for c in password):
        score += 10
    else:
        print("Add lowercase letters❌")

    if any(c.isupper() for c in password):
        score += 10
    else:
        print("Add uppercase letters❌")

    if any(c.isdigit() for c in password):
        score += 20
    else:
        print("Add numbers❌")

    if any(c in string.punctuation for c in password):
        score += 30
    else:
        print("Add special characters❌")

    return score

   d+o
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(12))

    return password

choice = input("Choose an option:\n1- Check Password\n2- Generate Password\nEnter 1 or 2: ")

if choice == "1":
    password = input("ENTER YOUR PASSWORD: ")
    score = check_password(password)

    print("Score:", score)

    if score <= 40:
        print("Weak Password 🔴")
    elif score <= 70:
        print("Medium Password 🟡")
    else:
        print("Strong Password 🟢")

elif choice == "2":
    print("Generated Password:", generate_password())

else:
    print("Invalid choice ❌")

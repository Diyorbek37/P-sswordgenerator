import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("Password Generator")


    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be positive!")
        else:
            print(f"Generated Password: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number.")











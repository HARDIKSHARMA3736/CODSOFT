import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length > 0:
                break
            else:
                print("Please enter a positive length.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()

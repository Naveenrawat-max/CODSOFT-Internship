import random
import string


def generate_unique_password(length):
    """Generate a random and unique password of the given length."""

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    remaining_length = length - len(password)
    password += ''.join(random.choice(string.printable)
                        for _ in range(remaining_length))

    password_list = list(password)
    random.shuffle(password_list)
    unique_password = ''.join(password_list)

    return unique_password


def main():
    length = int(input("Enter the desired length of the password: "))

    password = generate_unique_password(length)

    print("Your unique password is:", password)


if __name__ == "__main__":
    main()

import random
import string
import pyperclip  # install with: pip install pyperclip


# Returns all possible characters in a password as a list
def create_character_list():
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_characters = letters + digits + punctuation
    return list(all_characters)


# Returns the password as a string
def create_password():
    password_length = int(input("How many digits should the password have? "))
    password = []
    all_characters = create_character_list()
    for _ in range(0, password_length):
        sign = random.randint(0, len(all_characters) - 1)
        password.append(all_characters[sign])
    password = "".join(password)
    return password


# Outputs the password
def print_password(password):
    print(f"Your password is:\n{password}")


# Copies the password on request
def copy_password(password):
    copy_to_clipboard = input("Do you want to copy the password? (y|n) ")
    if copy_to_clipboard == "y":
        pyperclip.copy(password)


# Calls up all necessary functions
def main():
    password = create_password()
    copy_password(password)
    print_password(password)


if __name__ == "__main__":
    main()

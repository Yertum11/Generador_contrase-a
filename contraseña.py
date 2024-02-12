def get_valid_word(word):
    """
    Ensures that the word has at least 2 characters.
    If it's longer, it will be truncated to 2 characters.
    If it's shorter, it will be padded with 'X'.
    """
    if len(word) < 2:
        word = "X" + word
    elif len(word) > 2:
        word = word[:2]
    return word


def generate_password():
    """
    Prompts the user for three words, validates them, and generates the password.
    """
    word1 = get_valid_word(input("Enter the first word: "))
    word2 = get_valid_word(input("Enter the second word: "))
    word3 = get_valid_word(input("Enter the third word: "))

    password = word1 + word2 + word3
    print("The password is:", password)
    return password


def check_password(password, user_password):
    """
    Verifies the length and correctness of the user-entered password.
    """
    if len(user_password) < len(password):
        print("Missing", len(password) - len(user_password), "characters")
    elif len(user_password) > len(password):
        print("Excess", len(user_password) - len(password), "characters")
    elif user_password == password:
        print("Correct password")
    else:
        print("Incorrect password")


def main():
    """
    Main function that calls the above functions to execute the program.
    """
    generated_password = generate_password()
    user_password = input("Enter the password: ")
    check_password(generated_password, user_password)


# Call to the main function
if __name__ == "__main__":
    main()

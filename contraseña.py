def generate_password(word1, word2, word3):
    # Validate the length of each word
    validate_word_length(word1)
    validate_word_length(word2)
    validate_word_length(word3)

    # Fill words with 'X' if they have less than 2 characters
    word1 = word1.ljust(2, 'X')
    word2 = word2.ljust(2, 'X')
    word3 = word3.ljust(2, 'X')

    # Generate password
    password = ''.join([word1[0], word2[0], word3[0], word1[1], word2[1], word3[1]])

    return password

def validate_password(user_password, generated_password):
    # Validate the length of the password
    if len(user_password) < len(generated_password):
        print(f"Missing {len(generated_password) - len(user_password)} characters")
    elif len(user_password) > len(generated_password):
        print(f"Extra {len(user_password) - len(generated_password)} characters")
    else:
        # Check if the password is correct
        if user_password == generated_password:
            print("Correct password")
        else:
            print("Incorrect password")

def validate_word_length(word):
    # Validate the length of the word
    if 4 <= len(word) <= 8:
        print(f"The word '{word}' is correct.")
    elif len(word) < 4:
        print(f"Missing letters. Only has {len(word)} letters: {word}")
    else:
        print(f"Extra letters. Has {len(word)} letters: {word}")

# Request words from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

# Validate words and generate password
generated_password = generate_password(word1, word2, word3)
print("The generated password is:", generated_password)

# Request password from the user and validate it
user_password = input("Enter the password: ")
validate_password(user_password, generated_password)

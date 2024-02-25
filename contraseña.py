def generate_password(word1, word2, word3):
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

# Request words from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")

# Generate password and display it to the user
generated_password = generate_password(word1, word2, word3)
print("The generated password is:", generated_password)

# Request password from the user and validate it
user_password = input("Enter the password: ")
validate_password(user_password, generated_password)



# Call to the main function
if __name__ == "__main__":
    main()

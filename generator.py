import random


def generate_password(total_letters, total_symbols, total_numbers):
    """Function to generate a randomized password based on required letters, symbols & numbers."""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = ""
    randomised = "Y"
    final_password = ""
    # For Letters
    for count in range(total_letters):
        password += letters[random.randint(0, len(letters) - 1)]  # Alternative can be choice()

    # For Symbols
    for count in range(total_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]

    # For Numbers
    for count in range(total_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]

    final_password = randomizer(password)
    print(f"\nPassword: {final_password}")
    while randomised.upper() == "Y":
        randomised = input("\nDo you want to shuffled the password (Y/N): ").upper()
        if randomised == "Y":
            final_password = randomizer(final_password)
            print(f"\nPassword: {final_password}")
        elif randomised == "N":
            pass
        else:
            print("\nWrong parameter! Try again.")


def randomizer(current_password):
    """Function to randomize the password."""
    randomised_password = [character for character in current_password]
    password = ""
    random.shuffle(randomised_password)
    for character in randomised_password:
        password += character
    return password

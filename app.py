from random import randint
from pyperclip import copy

passwordLength = int(input("Password Length: "))
passwordOptions = str(
    input(
        """Password options:
[ L ] Letters
[ D ] Digits
[ S ] Symbols

Options: """
    )
    .strip()
    .upper()
)

splitedPasswordOptions = list(passwordOptions)

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "1234567890"
symbols = """*()[]{}!@#$%&*/\+=-~^:;.,?-_'"|><`'*"""

selected = ""

for option in splitedPasswordOptions:
    if option == "L":
        selected += letters
    elif option == "D":
        selected += digits
    elif option == "S":
        selected += symbols
    else:
        print("This option does not exist!")
        exit()

password = ""

for character in range(0, passwordLength):
    randomCharacter = randint(0, len(selected) - 1)
    password += selected[randomCharacter]
copy(password)

print(f"Your generated password is: {password}")
print("The password has been copied to your clipboard!")
input("Press any key to continue...")

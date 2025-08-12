import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spl_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    passLength = int(input("Enter the password length"))
    symbolsNeeded = int(input("Enter the count of Symbols to be included"))
    numNeeded = int(input("Enter the count of Number to be included"))

    passStr = ""
    letterLength = passLength - int(symbolsNeeded) - int(numNeeded)

    if letterLength < 0:
        print("Invalid password length inputs given, please check")
        return

    for number in range(1, letterLength + 1):
        passStr += random.choice(letters)

    for number in range(1, symbolsNeeded + 1):
        passStr += random.choice(spl_chars)

    for number in range(1, numNeeded + 1):
        passStr += random.choice(numbers)
    
    print(passStr)

generate_password()

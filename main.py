import random
print("Welcome to Password Generator")
letters_number = int(input("How many letters to be in your password? \n"))
symbols_number = int(input("How many symbols to be in your password? \n"))
numbers_number = int(input("How many numbers to be in your password? \n"))
letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ':', ';', '"',
          "'", '<', '>', ',', '.', '/', '?', '\\', '|']
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Your password is: ")
password_list = []
for i in range(1, letters_number + 1):
    char = random.choice(letter)
    password_list += char
for i in range(1, symbols_number + 1):
    char = random.choice(symbol)
    password_list += char
for i in range(1, numbers_number + 1):
    char = str(random.choice(number))
    password_list += char
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)

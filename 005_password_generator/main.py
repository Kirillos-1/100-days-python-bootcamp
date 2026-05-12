import random
import string

letters = list(string.ascii_letters)
symbols = list("!#$%&()*+")
numbers = list(string.digits)

print("Welcome to the PyPassword Generator!\n")

n_letters = int(input("How many letters would you like? "))
n_symbols = int(input("How many symbols would you like? "))
n_numbers = int(input("How many numbers would you like? "))

password = []

for _ in range(n_letters):
    password.append(random.choice(letters))

for _ in range(n_symbols):
    password.append(random.choice(symbols))
    
for _ in range(n_numbers):
    password.append(random.choice(numbers))
    
random.shuffle(password)
password = ''.join(password)

print(f"Your password is: {password}")
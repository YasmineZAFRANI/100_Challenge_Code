import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+'

# Demander le nombre de chaque type de caractère
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Mode "Facile" : Lettres, puis symboles, puis chiffres (ordre fixe)
easy_password = ""

for _ in range(nr_letters):
    easy_password += random.choice(letters)

for _ in range(nr_symbols):
    easy_password += random.choice(symbols)

for _ in range(nr_numbers):
    easy_password += random.choice(numbers)

print(f"Easy password: {easy_password}")

# Mode "Difficile" : Mélange des caractères
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)  

hard_password = "".join(password_list)
print(f"Hard password: {hard_password}")

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
i = 0
while i < nr_letters:
    r = random.randint(0, len(letters) - 1)
    password += letters[r]
    i += 1
i = 0
while i < nr_symbols:
    r = random.randint(0, len(symbols) - 1)
    password += symbols[r]
    i += 1
i = 0
while i < nr_numbers:
    r = random.randint(0, len(numbers) - 1)
    password += numbers[r]
    i += 1




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

totalnum = nr_numbers + nr_symbols + nr_letters
password2 = []
index = []

# generate a base string for password as a list (will turn to string later)
i = 0
while i < totalnum:
    password2.append("*")
    i += 1
# for the index of the base password, will pop items as assigned
for a in range(0,totalnum):
    index.append(a)


i = 0
z = totalnum - 1
while i < nr_letters:
    r = random.randint(0, len(letters) - 1)     #random number to choose letter
    r1 = random.randint(0,z)                    #random number to pop an index number
    j = index.pop(r1)                           #assign the random index for the place of the password to change
    password2[j] = letters[r]                   #insert random letter to that place
    i += 1
    z -= 1
i = 0
while i < nr_symbols:                           #repeat for symbol and numbers...
    r = random.randint(0, len(symbols) - 1)
    r1 = random.randint(0, z)
    j = index.pop(r1)
    password2[j] = symbols[r]
    i += 1
    z -= 1
i = 0
while i < nr_numbers:
    r = random.randint(0, len(numbers) - 1)
    r1 = random.randint(0, z)
    j = index.pop(r1)
    password2[j] = numbers[r]
    i += 1
    z -= 1

# Change the list to string
password_hard = ""
for i in password2:
    password_hard += i


print(password)
print(password_hard)




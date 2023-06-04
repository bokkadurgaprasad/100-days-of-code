#Password Generator Project
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
           'o','p','q','r','s','t','u','v','w','x','y','z'
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to PyPassword Generator!")
nr_lt = int(input("How many letters would you like in your password?\n"))
nr_sy = int(input("How many symbols would you like?\n"))
nr_nm = int(input("How many numbers would you like?\n"))

password_lst = []

for ch in range(1, nr_lt + 1):
    password_lst.append(random.choice(letters))

for ch in range(1, nr_sy + 1):
    password_lst+= random.choice(symbols)

for ch in range(1, nr_nm + 1):
    password_lst.append(random.choice(numbers))

random.shuffle(password_lst)

password = ""
for c in password_lst:
    password += c

print(password)
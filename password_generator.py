import random
from pkgutil import resolve_name

print("Welcome to password generator !!!")
x = int(input("How many letters would you like in your password ?"))
y = int(input("How many special symbols would you like in your password ?"))
z = int(input("How many numbers would you like in your password ?"))
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                         'N', 'O', 'P', 'Q', 'R', 'S', 'T',]
list3 = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
                        '[', ']', '{', '}', '|', ';', ':', '"', ',', '.', '<', '>', '?', '/',
                        '`', '~', '\\', '\'']
list4 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list0 = [''] * x
list9 = [''] * y
list8 = [''] * z
for q in range(0,x):
    a = random.choice(list1)
    list0[q] = a
for w in range(0,y):
    b = random.choice(list3)
    list9[w] = b
for e in range(0,z):
    c = random.choice(list4)
    list8[e] = c
list5 = list9+list8+list0
random.shuffle(list5)
for i in list5:
    print(i,end='')






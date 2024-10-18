import random
from random import randint

x = input("Enter the names of the people(please separate each name with a comma")
y = x.split(",")
print(y)
a = len(y)
b = random.randint(0,a-1)
print("The bill shall be payed by (drumroll........)\n")
print(y[b])


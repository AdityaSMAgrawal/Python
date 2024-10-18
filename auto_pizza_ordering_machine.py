x = int(input("Which size pizza do you want ? \n 1)Small \n 2)Medium \n 3)Large"))
s = 0
if x == 1:
    s = 100
    z = int(input("Do you want pepperoni ?"))
    if z ==1 :
        s = 130
    else :
        s = 100
elif x == 2:
    s = 200
    z = int(input("Do you want pepperoni ?"))
    if z == 1:
        s = 250
    else:
        s = 200
else:
    s = 300
    z = int(input("Do you want pepperoni ?"))
    if z == 1:
        s = 350
    else:
        s = 300
y = int((input("Do you want extra cheese ?)")))
if y ==1:
    s = s + 20
else:
    s = s+0
print(s)

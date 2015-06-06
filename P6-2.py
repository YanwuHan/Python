__author__ = 'hanyw'
from random import randrange
print("INTEGER DIVISION")
while(True):
    a = randrange(5)
    b = randrange(5)
    c = a*b
    try:
        print(c,"/",end='')
        print(b,"=",end="")
        ans=int(input(""))
        if ans==a:
            print("CORRECT!")
        else:
            print("INCORRECT!")
    except ValueError:
        print("Please enter Integers Only!")


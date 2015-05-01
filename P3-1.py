__author__ = 'hanyw'
def bunnyEars(n):
    if n == 0:
        return 0
    else:
        if n%2 == 0:
            return bunnyEars(n-1) + 2
        else:
            return bunnyEars(n-1) + 3
number = input("Enter: ")
number
print(bunnyEars(number))
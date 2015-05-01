__author__ = 'hanyw'
def count_frequency(mylist):
    mydict = {}
    for i in mylist:
        if i not in mydict:
            mydict.setdefault(i, 1)
        else:
            mydict[i] = mydict[i]+1
    print(mydict)
list = []
print("Enter a list:(enter 0 to end)")
while True:
    s = input("")
    if s == '0':
        break
    else:
        list.append(s)
count_frequency(list)

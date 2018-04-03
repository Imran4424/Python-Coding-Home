
a = int(input("enter int num: "))
b = int(input("enter int num: "))
c = int(input("enter int num: "))

if(a>b):
    if(b>c):
        print("Minimum is:", c)
    else:
        print("Minimum is:", b)

else:
    if(a>c):
        print("Minimum is:", c)

    else:
        print("Minimum is:", a)

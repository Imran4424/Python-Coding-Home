
a = int(input("enter an int: "))
b = int(input("enter an int: "))
c = int(input("enter an int: "))


if(a>b):
    if(b>c):
        print("Medium is: ",b)

    else:
        print("Medium is: ",c)

else:
    if(a>c):
        print("Medium is: ",a)
    
    else:
        print("Medium is: ",c)

def maximum(x,y,z):
    if(x>y):
        if(x>z):
            return x
        else:
            return z

    else:
        if(y>z):
            return y
        else:
            return z


a = int(input("enter an int: "))
b = int(input("enter an int: "))
c = int(input("enter an int: "))


max_value = maximum(a,b,c)

print()
#1+2+3+....+n

n = int(input("enter an int: "))

sum = 0

for i in range(1,n+1):
    sum += i


print("The summation is: ", sum)
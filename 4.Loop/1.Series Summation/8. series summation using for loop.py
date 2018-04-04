# 1^1+2^2+3^3+...+n^n

n = int(input("enter an int: "))

summation = 0

for i in range(1, n+1):

    summation += pow(i, i)


print("The Summation is: ", summation)

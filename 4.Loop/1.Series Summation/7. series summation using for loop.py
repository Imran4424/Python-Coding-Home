# 1^3+2^3+3^3+...+n^3

n = int(input("enter an int: "))

summation = 0

for i in range(1, n+1):

    summation += pow(i, 3)


print("The Summation is: ", summation)

# 1^2+2^2+3^2+...+n^2

n = int(input("enter an int: "))

summation = 0

for i in range(1,n+1):
    
    summation += pow(i,2)


print("The Summation is: ", summation)


# 2+4+6+....+n

n = int(input("enter an int: "))

summation = 0   #don't use sum as a variable cause it's a build in function

for i in range(2,n+1,2):

    summation += i
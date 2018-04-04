'''
indentation is the biggest factor of python programming



'''


def factorial(n):
    if(n==1):
        return 1

    return n*factorial(n-1)


n = int(input("enter an int: "))

result = factorial(n)

print("Factorial of that number is: ",result)
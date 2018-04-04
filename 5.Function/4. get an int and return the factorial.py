'''
indentation is the biggest factor of python programming

it detects the current function, current loop and current if-else statement

so we need to use it wisely

'''


def factorial(n):
    if(n==1):
        return 1

    return n*factorial(n-1)


n = int(input("enter an int: "))

result = factorial(n)

print("Factorial of that number is: ",result)
# Factorial of a given Number


def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

num = int(input("Enter Number=>"))
print(f"Factorial of a number {num} is "+str(factorial(num)))
        


# Program - 1

# This program is used to find the multiplication of two numbers entered by the user –
# using if elif statements without arithmetic operator

'''
# Recursion Method
x = int(input("First Number=>"))
y = int(input("Second Number=>"))

def findProduct(x,y):
    if y < 0:
        return -findProduct(x,-y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x+findProduct(x,y-1)

print("Product of two numbers is",findProduct(x,y))
print(type(findProduct(x,y)))
'''

# For Loop
x = int(input("First Number=>"))
y = int(input("Second Number=>"))
product = 0
for i in range(1,y+1):
    product = product + x
print("Product of two numbers is",product)


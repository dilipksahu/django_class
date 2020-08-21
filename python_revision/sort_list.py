# Write a program in Python to execute the Bubble sort algorithm.

# 1. manual method
def sortList(a):
    b = len(a)-1
    for x in range(b):
        for y in range(b-x):
            if a[y] > a[y+1]:
                a[y],a[y+1] = a[y+1],a[y]
    return a

n = list(map(int,input("enter list of numbers=>").rstrip().split()))
print(n)
print(sortList(n))
                

# 2. buit-in function

def sortList(a):
    a.sort()
    return a
n = list(map(int,input("enter list of numbers=>").rstrip().split()))
print(n)
print(sortList(n))

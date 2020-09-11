'''
Input Format

A single line containing the space separated values of N and M.
Mat size must be X. ( is an odd natural number, and  is  times .)
Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''
def welcome(row,col):
    width = col
    # Upper Triangle
    for i in range(0,row//2):
        pattern = ".|." * ((2*i)+1)
        print(pattern.center(width,"-"))

    # Middle Part
    print("WELCOME".center(width,"-"))

    # Inverted Triangle
    for j in range(row//2,0,-1):
        pattern = ".|." * ((2*j)-1)
        print(pattern.center(width,"-")) 
        
n,m = map(int,input().split())
welcome(n,m)

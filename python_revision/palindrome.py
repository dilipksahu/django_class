# Write a program in Python to check if a sequence is a Palindrome.

def palindrome(a):
    n = len(a)
    if n == 1:
        print("Enter digit keeping space.")
    else:
        b = a[::-1]
        if a == b:
            print("Penlindrome")
        else:
            print("Not Palindrome")

a = list(map(int,input("Input=>").rstrip().split()))
palindrome(a)
        

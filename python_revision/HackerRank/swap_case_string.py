'''
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
'''

def swap_case(s):
    string = str(s)
    newstring = ""
    for i in string:
        if i.isupper():
            newstring += i.lower()
        elif i.islower():
            newstring += i.upper()
        elif i.isspace():
            newstring += i
        else:
            newstring += i
    return newstring

if __name__ == '__main__':
    s = input("String=>")
    result = swap_case(s)
    print(result)

# ****************** 2nd method *******************************

string = input("String=>")
print(string.swapcase())



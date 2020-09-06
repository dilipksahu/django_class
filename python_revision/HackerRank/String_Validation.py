
'''
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters,
alphanumeric characters, digits, etc.

Sample Input

qA2

Sample Output

True
True
True
True
True
'''

# ************* method-1 ********************
if __name__ == '__main__':
    s = input("Input:")
    
    func =  [str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]
    
    for fn in func:
        for ch in s:
            if fn(ch):
                print(True)
                break
        else:
            print(False)
            
            
# ************* method-2 ***********************
S = input("Input:")
print(any([char.isalnum() for char in S]))
print (any([char.isalpha() for char in S]))
print (any([char.isdigit() for char in S]))
print (any([char.islower() for char in S]))
print (any([char.isupper() for char in S]))

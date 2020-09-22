'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    print(myStr)
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = myStr[size:x:-1]+myStr[x:size]
        print( '--'*x + '-'.join(line) + '--'*x)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

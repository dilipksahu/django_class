'''
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers.
Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Sample Input 0

2
1 2

Sample Output 0

371308163193441065

Python offers hash() method to encode the data into unrecognisable value.
'''
'''
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuplex = tuple()
    for i in range(n):
        for i in integer_list:
            tuplex = tuplex + (i,)
    
    print(str(hash(tuplex)))
    
'''
def fizz_buzz(num):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    elif (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    else:
        print(f"{num}")

num = int(input())
print(fizz_buzz(num))

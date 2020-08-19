'''
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .

Return

int: the sum of all array elements
'''

def aVeryBigSum(ar):
    total = 0
    for x in range(0,len(ar)):
        total = total + ar[x]
    return total

ar = list(map(int, input("Enter Big Number separated by space=>").rstrip().split()))

result = aVeryBigSum(ar)
print(ar)
print("Sum: ",result)

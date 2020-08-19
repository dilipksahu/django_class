'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
'''

def diagonalDifference(arr):
    left, right = 0, 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if (i==j):
                left += arr[i][j]
            if (i+j) == (len(arr)-1):
                right += arr[i][j]
    diff = abs(left - right)
    return diff
n = int(input("2D matrix shape=>").strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input("2D Square matrix=>").rstrip().split())))
result = diagonalDifference(arr)
print("Diagonal Absolute Diff: ",result)




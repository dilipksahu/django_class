'''
Given a 6 x 6  2D Array,arr :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in A is a subset of values with indices falling in this pattern in arr's 's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
The array will always be 6 x 6.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19

Explanation:
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4

'''
def hourglassSum(arr):
    maxSum = -9 * 7
    print(arr)
    for i in range(4):
        for j in range(4):
            # For Top Line
            top = sum(arr[i][j:j+3])
            
            # For Middle Point
            mid = arr[i+1][j+1]
            
            # For Bottom Line
            bottom = sum(arr[i+2][j:j+3])
            
            totSum = top + mid + bottom
            if totSum > maxSum:
                maxSum = totSum
    return maxSum
    
arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)

'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

Sample Input

1 2 3 4 5
Sample Output

10 14
Explanation

The numbers are 1,2, 3, 4, and 5. Calculate the following sums using four of the five integers:

Sum everything except 1, the sum is 2+3+4+5=14.
Sum everything except 2, the sum is 1+3+4+5=13.
Sum everything except 3, the sum is 1+2+4+5=12.
Sum everything except 4, the sum is 1+2+3+5=11.
Sum everything except 5, the sum is 1+2+3+4=10.

'''

def minMaxSum(arr):
    arr.sort()
    minn = arr[0] + arr[1] + arr[2] + arr[3]
    maxx = arr[1] + arr[2] + arr[3] + arr[4]
    print("MIn Sum:",minn,"Max Sum:",maxx)

n = list(map(int, input("Enter any 5 numbers=>").rstrip().split()))
minMaxSum(n)
    

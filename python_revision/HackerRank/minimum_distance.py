'''
We define the distance between two array values as the number of indices between the two values.

Given , find the minimum distance between any pair of equal elements in the array.

If no such value exists, print -1 .

For example, if a = [3,2,1,2,3], there are two matching pairs of values:3 and 2 . The indices of the 's are  and , so their distance is .

The indices of the 3's are i = 0 and j = 4 and , so their distance is d[i,j] = |j - i| = 4.

The indices of the 2's are i = 1 and j = 3, so their distance is d[i,j] = |j-i| = 2.

Sample Input

6
7 1 3 4 1 7

Sample Output

3

'''

n = int(input())
A = list(map(int,input().split()))

ans = 9999999999
for i in range(n):
    for j in range(n):
        if A[i] == A[j] and i != j:
            ans = min(ans, abs(i - j))

if ans == 9999999999:
    ans = -1
print(ans)

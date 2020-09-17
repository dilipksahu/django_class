'''
Input Format

The first line contains two space-separated integers n and d, the size of a and the number of left rotations you must perform.
The second line contains n space-separated integers a[i].

Sample Input

5 4
1 2 3 4 5

Sample Output

5 1 2 3 4
'''

def rotLeft(a, d):
    b = []
    for i in range(d,len(a)):
        b.append(a[i])
    for i in range(d):
        b.append(a[i])
    return b

# we can implement the function in one line with array slicing:
def solve(a, d):
	return(a[d:]+a[:d])

nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)
print(result)

result = solve(a, d)
print(result)

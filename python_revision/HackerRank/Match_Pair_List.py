'''
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3
'''

def sockMerchant(n, ar):
    c = 0
    d = {}
    for i in ar:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for key in d:
        c = c + d[key]//2
        #c = c + int(d[key]/2)   # Same as above
    return c


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)

print(result)

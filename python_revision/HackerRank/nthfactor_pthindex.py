'''
Determine the factors of a number (i.e., all positive integer values that
evenly divide into a number) and then return the p element of the
list, sorted ascending. If there is no p element, return 0.
Example
n = 20
p = 3
The factors of 20 in ascending order are {1, 2, 4, 5, 10, 20}. Using 1-
based indexing, if p = 3, then 4 is returned. If p > 6, 0 would be
returned.

Sample Case 0
Sample Input 0
STDIN Function
----- --------
10 → n = 10
3 → p = 3
Sample Output 0
5
Explanation 0
Factoring n = 10 results in {1, 2, 5, 10}. Return the p = 3 factor, 5, as
the answer.

'''
# Method - 1
def pthFactor(n,p):
    factor = []
    for i in range(1,n+1):
        if n%i == 0:
            factor.append(i)
    if p > len(factor):
        return 0
    else:
        return factor[p-1]
    
# Method - 2

def pth_Factor(n,p):
    factor = []
    for i in range(1,n+1):
        if n%i == 0:
            factor.append(i)
    try:
        output = factor[p-1]
    except IndexError:
        return 0
    else:
        return output



n = int(input())
p = int(input())

result = pthFactor(n,p)
print(result)
print("*****************************************")
output = pth_Factor(n,p)
print(output)





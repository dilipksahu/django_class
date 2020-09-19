'''
Given a list of strings, concatenate those strings into the alphabetically
smallest string possible. For example, 'a' < 'b', 'ab' < 'ac' and 'ab' < 'abc'.

Example
substrings = ['a','bd','ac','cd']
Return 'aacbdcd'.

Sample Input
STDIN Function
----- -----
3 → substrings[] size n = 3
abc → substrings = ['abc', 'ab', 'bc']
ab
bc

Sample Output
ababcbc
'''


def smallestString(s,n):
    s.sort(reverse = False)
    string = ""
    for i in range(n):
        string += s[i]
    return s,string


n = int(input())

substrings = []
for i in range(n):
    substrings.extend(list(map(str, input().rstrip().split())))

result = smallestString(substrings,n)
print(result[0],"\n",result[1])

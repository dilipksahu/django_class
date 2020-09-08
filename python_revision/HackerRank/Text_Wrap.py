'''
You are given a string S  and width W.
Your task is to wrap the string into a paragraph of width W.

Input Format

The first line contains a string,S .
The second line contains the width,W .

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
import textwrap

# Type1 - Paragraph
def wrapPara(string, max_width):
    s = textwrap.fill(string,max_width)
    return s

# Type2 - List
def wrapList(string, max_width):
    s = textwrap.wrap(string,max_width)
    return s

if __name__ == '__main__':
    string, max_width = input(), int(input())
    resultpara = wrapPara(string, max_width)
    resultlist = wrapList(string, max_width)
    print("Paragraph")
    print(resultpara)
    print("List")
    print(resultlist)

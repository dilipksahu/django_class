'''
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs
in the given string. String traversal will take place from left to right,
not from right to left.

NOTE: String letters are case-sensitive.

Sample Input

ABCDCDC
CDC

Sample Output

2
'''
# **************** 1 ***********************
s1="gabcdfahibdgsabc hi kilg hi"
s2="hi"
count=0
l2=len(s2)
for i in range(len(s1)):
    if s1[i]==s2[0]:   
        end=i+l2
        sub1=s1[i:end]
        if s2==sub1:
            count+=1
print ("Manual:",count)

# ******************* 2 *******************
s1="gabcdfahibdgsabc hi kilg hi"
s2="hi"
count=0
l1 = len(s1)
l2=len(s2)
for i in range((l1 - l2) + 1):
    if s1[i:i+l2] == s2:  
      count+=1
print ("Simple Manual:",count)
# ******************************************************
# find first match index
s1="gabcdfahibdgsabc hi kilg hi"
s2="hi"
num = s1.find(s2)
print("String Function:",num)

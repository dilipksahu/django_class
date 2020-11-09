'''
Dothraki are planning an attack to usurp King Robert's throne.

King Robert learns of this conspiracy from Raven and plans to lock

the single door through which the enemy can enter his kingdom.

But, to lock the door he needs a key that is an anagram of a palindrome.

He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.

For example, given the string s = [aabbccdd], one way it can be arranged

into a palindrome is abcddcba.

Sample Input 0

aaabbbb

Sample Output 0

YES

Explanation 0

A palindromic permutation of the given string is bbaaabb.

'''

if __name__ == '__main__':
    string = input()
    found = True
    # Write the code to find the required palindrome and then assign
    # the variable 'found' a value of True or False
    oddCnt = 0
    letterCnt = [0] * 26
     
    for letter in string:
        letterCnt[ord(letter)-ord('a')] += 1
     
    for cnt in letterCnt:
        oddCnt += cnt % 2
         
    if oddCnt > 1:
        found = False
 
    if not found:
        print("NO")
    else:
        print("YES")

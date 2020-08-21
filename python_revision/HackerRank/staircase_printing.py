'''
Consider a staircase of size :

   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size .

'''

def staircase(n):
    m = n - 1
    for i in range(n):
        print(" "*(m)+("#")*(i+1))
        m = m - 1
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)

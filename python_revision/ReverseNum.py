# Reverse of a Number


def reverseNum(n):
    rev_num = 0
    while(n > 0): 
        rem = n % 10
        rev_num = rev_num * 10 + rem
        n = n // 10
    print("Method-1")  
    print(rev_num)


def reverse_Num(n):
    rev_num = 0
    for i in range(len(str(n))):
        a = n % 10
        rev_num = rev_num * 10 + a
        n = n // 10
    print("Method-2") 
    print(rev_num)


def reverseNumStr(n):
    a = str(n)
    rev_num = a[::-1]
    print("Method-3")
    print(rev_num)
        



num = int(input("Number=>"))
reverseNum(num)
reverse_Num(num)
reverseNumStr(num)

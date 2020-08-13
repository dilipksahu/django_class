# Find neon numbers for given number


def neonNo(num):
    sumOfNum = 0
    sqr = num**2
    while sqr > 0:
        sumOfNum = sumOfNum + sqr%10
        sqr = sqr//10
    if num == sumOfNum:
        print("Neon Number")
    else:
        print("Not a Neon Number")

neonNo(int(input("Enter Number=>")))
        

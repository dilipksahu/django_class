# Print prime numbes between 1 to 100
'''
start = 1
end = 100

for num in range(start,end+1):
    if num > 1:
        for i in range(2,num//2 +2):
            if (num%i)==0:
                break
            else:
                if i == num//2 + 1:
                    print(num)
'''
    

def primeNo(start,end):
    for num in range(start,end+1):
        if num > 1:
            for i in range(2,num//2 +2):
                if (num%i)==0:
                    break
                else:
                    if i == num//2 + 1:
                        print(num)

primeNo(1,100)

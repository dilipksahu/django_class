# Print ABCD Pyramid as no of aplhabet provided by user

num = 65
n = 5
for i in range(n-1,-2,-1):
    for j in range(1,n-i+2):
        if j == 1:
            if (num % 2) != 0:
                ch = chr(num)
                print(" "*i + ch *(j),end=" ")
                num = num + 1
            print()
            else:
            
            


def welcome(n,m):
    for i in range(n//2):
        for j in range(m):
            print("-"*((m//2-1)-(3*j))+".|."*((i*2)+1)+"-"*((m//2-1)-(3*j)))
        break

welcome(9,27)

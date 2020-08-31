
l = [5,4,6,-8,9,0,5,4,12,11]

def largestNo(l):
    if l[0] > l[1]:
        first,second = l[0],l[1]
    else:
        first,second = l[1],l[0]

    for i in l[2:]:
        if i > second:
            if i > first:
                second = first
                first = i
            else:
                second = i
        
        
    print(first , second)

largestNo(l)
        
'''
def runner_up(l):
    first = l[0]
    second = l[1]
    for x in range(len(l)):
        if l[x] > first:
            second = first
            first = l[x]
        if (l[x] < first and l[x] > second):
            second = l[x]
    print(second)
            

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runner_up(arr)
'''

# Count the occurences of a particular element in the list and
# output highest occuring element

days= ['sun','mon','tue','wed','mon','thu','fri','sat','mon']

# ************************************************************
def findMax(days):
        #Output: Mon since it occured three times
        seen = {}
        dupes = []
        for x in days:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
        #Keymax = max(seen, key=seen.get)
        return dupes,seen[dupes[0]]

print(findMax(days)

# *************************** Manual way ***************************************
      
def findMax(days):
    dic = {}
    lis = []
    maxkey = ""
    for i in days:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    lis = list(dic.values())
    if lis[0] > lis[1]:
        l1 = lis[0]
    else:
        l1 = lis[1]
    for i in range(2,len(lis)):
        if lis[i] > l1:
            l1 = lis[i]
    for k in dic:
        if dic[k] == l1:
            maxkey= k
            
    print(dic)
    print(maxkey)
    
findMax(days)

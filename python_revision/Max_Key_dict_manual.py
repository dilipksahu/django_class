#2.Count the occurences of a particular element in the list and
# output highest occuring element

days= ['sun','mon','tue','wed','sun','thu','fri','sat','sun']

def findMax(days):
    dict = {}
    for i in days:
        if i not in dict:
            dict[i] = 1
        else:
            if i in dict:
                dict[i] = dict[i] + 1
    keylist = []
    for key,val in dict.items():
        keylist.append(key)
        maxkey = keylist[0]
        for s in range(1,len(keylist)):
            if dict[maxkey] < dict[keylist[s]]:
                maxkey = keylist[s]
                
    print(dict)
    print(maxkey)
    
findMax(days)

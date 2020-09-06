# Find the duplicate elements in list and their counts
# List 

def duplicate(x):
    uniq = []
    dup = []
  
    for i in x:
        if i not in uniq:
            uniq.append(i)
        else:
            dup.append(i)
    print("list:"+str(x)+"\nDuplicate:"+str(dup))
            
l = [1,0,5,8,5,1,2,0,'a','a']
duplicate(l)

# dictioary

def duplicate(x):
    dic = {}
    dup = []
  
    for i in x:
        if i not in dic:
            dic[i] = 1
        else:
            if dic[i] == 1:
                dup.append(i)
            dic[i] += 1
    print("Duplicate:"+str(dup)+"\nConuts:"+str(dic))
            
l = [1,0,5,8,5,1,2,0,'a','a']
duplicate(l)

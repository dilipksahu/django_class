
# Q 1. Find out the maximum number from the list without using any built-in methods

l = [2,5,8,6,1]

def largestElement(l):
    set(l)
    largest = l[0]
    for x in l:
        if x > largest:
            largest = x
    print("Largest Number: ",largest)
    return largest

#largestElement(l)


# Q 2. Find out the second maximum number from the above list

def secondLargest(l):
    largest = largestElement(l)
    seclarge = l[0]
    for x in l:
        if (x != largest) and (x > seclarge):
            seclarge = x
    print("Second Largest No: ",seclarge)

secondLargest(l)


# Q 3.Find out the key whose value is a second maximum number

d = [{'a':2}, {'b':5}, {'c':8}, {'d':6}, {'e':1}]

def secondMaxKey(d):
    mydict = {}
    for ele in d:
        for key,value in ele.items():
            mydict[key] = value
    maxx1 = max(mydict.values())
    maxx2 = 0
    for k,v in mydict.items():
        if (v > maxx2 and v < maxx1):
            maxx2 = v
            key2 = k 
    print(f"Second Largest Key:{key2} and value:{maxx2}")
  

secondMaxKey(d)









            
            

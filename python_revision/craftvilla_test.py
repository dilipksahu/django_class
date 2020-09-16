#1.Join items of given list using "and" and print the string
weekdays= ['sun','mon','tue','wed','thu','fri','sat']

def convertToString(weekdays):
        #Output: 'sun and mon and tue and..'
        string = ''
        for i in weekdays:
                if i == weekdays[-1]:
                        string = string + i 
                else:
                        string = string + i +" " + "and "
        return string
print(convertToString(weekdays))


#2.Count the occurences of a particular element in the list and
# output highest occuring element

days= ['sun','mon','tue','wed','mon','thu','fri','sat','mon']

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

print(findMax(days))


#3. Merging dictionaries - The resultant dict must contain all the items of both dict
# both dicts. If key is common then the value of key in resultant dict
# must be the sum of value in a and b

a = {'x':1,'y':2,'z':8}
b = {'a':4,'b':5,'x':6,'z':5}

def dictMerge(a,b):
    for i in b:
        if i in a:
            b[i] = b[i] + a[i]
    # merge and replace a with b
    c = {**a,**b}
    print(c)
dictMerge(a,b)
        

#4. Item with highest value count
items = [{'apple':5},{'banana':8},{'orange':7},{'grapes':4}]

def itemWithHighestValue(items):
        #print the fruit name whose value is maximum
        mydict = {}
        for val in items:
                for key,value in val.items():
                        mydict[key] = value
        keymax = max(mydict, key=mydict.get)
        print(keymax + "-->" +str(mydict[keymax]))
                        

itemWithHighestValue(items)



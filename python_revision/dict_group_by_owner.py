'''
you need to convert dictionary values into keys and by grouping the values in
the form of list

example:
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}

'''


def group_by_owners(files):
    owner = {}
    l = []
    for key,val in files.items():
        if val not in owner:
            owner[val] = [key]
        else:
            owner[val].append(key)
            
    return owner

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))

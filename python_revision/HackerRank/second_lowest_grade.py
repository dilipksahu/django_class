'''
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
'''


'''

if __name__ == '__main__':
    records = {}
    stud_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
        
    s = records.values()
    l = sorted(s)
    u = l[-2]
    for key in records.keys():
        if records[key] == u:
            stud_list.append(key)

    for x in sorted(stud_list):
        print(x)
'''




score_list = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
print(new_list)
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")



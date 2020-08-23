'''
HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .

Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Input Format

The first line contains a single integer, , the number of students.
Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.

Sample Input 0

4
73
67
38
33
Sample Output 0

75
67
40
33
'''

def gradingStudents(grades):
    gd = []
    for x in grades:
        if x < 38:
            gd.append(x)
        if x >= 38:
            y = x
            if (y % 5) == 0:
                gd.append(y)
            else:
                for i in range(1,5):
                    y = y + 1
                    if (y % 5) == 0:
                        diff = y - x
                        if diff < 3:
                            gd.append(y)
                        else:
                            gd.append(x)
    return gd    
                    
grades_count = int(input("Total grades=>").strip())
grades = []

for _ in range(grades_count):
    grades_item = int(input("Enter grade one below other=>").strip())
    grades.append(grades_item)

result = gradingStudents(grades)

#for i in result:
print('\n'.join(map(str, result)))




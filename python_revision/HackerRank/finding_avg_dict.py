'''

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0

56.00

'''
if __name__ == '__main__':
    n = int(input("no of Students=>"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Name and marks seperated by space=>").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter Name to find Average marks=>")
    for key,value in student_marks.items():
        if key == query_name:
            avg = sum(value)/len(value)
    print("{:.2f}".format(avg))

import csv
import math



with open('Assets/student_grades.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

    '''for row in range(1, len(reader):
        if row[]
        average = row[1] + row[2] + row[3] + row[4]
        print(average)'''

with open('Assets/student_grades.csv') as file:
    reader1 = csv.DictReader(file)

    for row in reader1:
        print(row)

#calcAverage()

with open('Assets/student_grades.csv') as file:
    reader1 = csv.DictReader(file)

    '''for key, value in reader1.items():
        if key == 'Grade 1':
            print(value)'''
    
    for row in reader1:

        status = ''

        average = (int(row['Grade 1']) + int(row['Grade 2']) + int(row['Grade 3'])) / 3
        stdName = row['Student']

        grade = math.ceil(average)

        if grade > 70:
            status = 'passed'
        else:
            status = 'failed'

        print(f'{stdName} achieved an average grade of {grade} and so {status}')
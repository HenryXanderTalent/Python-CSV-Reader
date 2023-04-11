import csv

with open('Assets/student_grades.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
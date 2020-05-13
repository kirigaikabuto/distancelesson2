from utils import *
students=[]
n = int(input())
for i in range(n):
    line = input()
    newstudent=create_student(line)
    students.append(newstudent)

newstudent_line="arystan,19,1 2 3 4"
newstudent = create_student(newstudent_line)
students.append(newstudent)
print_arr(students)


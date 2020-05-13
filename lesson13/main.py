from utils import *
students=[]
student1=create_student("yerasyl,29,1 2 3 3 4")
student2=create_student("yerassyl123,30,1 2 3 4 5")
students.append(student1)
students.append(student2)

def list_students():
    print_arr(students)
    main()
def add_student():
    name = input("name:")
    age = input("age:")
    marks = input("marks:")
    line=f"{name},{age},{marks}"
    newstudent= create_student(line)
    students.append(newstudent)
    main()
def delete_student():
    name = input("name:")
    #code
    index=-1
    n = len(students)
    for i in range(n):
        student=students[i]
        if student['name']==name:
            index=i
            
    if index!=-1:
        students.pop(index)
        print(f"user with name {name} was deleted")
    else:
        print("no student with that name")
    main()
    
def main():
    print("[1]List Of students")
    print("[2]Add new student")
    print("[3]Delete student")
    print("[4]Update Student")
    print("[5]Exit")
    num = input()
    if num == "1":
        list_students()
    elif num =="2":
        add_student()
    elif num == "3":
        delete_student()
    else:
        exit()


main()
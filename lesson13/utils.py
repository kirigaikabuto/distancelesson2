def create_student(line):
    parts=line.split(",")
    name = parts[0]
    age = int(parts[1])
    marks_str = parts[2]
    marks_str_arr = marks_str.split(" ")
    marks_int_arr = [int(i) for i in marks_str_arr]
    d={}
    d['name']=name
    d['age']=age
    d['marks']=marks_int_arr
    return d
def print_arr(arr):
    for i in arr:
        print(i)
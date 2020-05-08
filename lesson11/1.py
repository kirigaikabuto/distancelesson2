# 3
# yerassyl,5 4 4 2
# kirito,5 4 3
# era,5 5 5 4 5
# 1
# china,5 4 3 3 2
n = int(input())#3
students=[]
for i in range(n):
    line = input()#yerassyl,5 4 4 2
    parts = line.split(",")#['yerassyl', '5 4 4 2']
    name = parts[0]#'yerassyl'
    marks_str = parts[1]#'5 4 4 2'
    marks_str_arr = marks_str.split(" ")#['5','4','4','2']
    marks_int_arr = [int(i) for i in marks_str_arr]#[5,4,4,2]
    d={}
    d['name']=name
    d['marks']=marks_int_arr
    students.append(d)

for i in students:
    name=i['name']
    marks=i['marks']
    sumi=0
    n = len(marks)
    for j in marks:
        sumi = sumi + j
    avg = sumi/n
    i['avg']=avg

maxi_avg =students[0]['avg']
mini_avg =students[0]['avg']
for i in students:
    if i['avg']>maxi_avg:
        maxi_avg = i['avg']
    if i['avg']<mini_avg:
        mini_avg = i['avg']

m = int(input())
newstudents=[]
for i in range(m):
    line = input()#yerassyl,5 4 4 2
    parts = line.split(",")#['yerassyl', '5 4 4 2']
    name = parts[0]#'yerassyl'
    marks_str = parts[1]#'5 4 4 2'
    marks_str_arr = marks_str.split(" ")#['5','4','4','2']
    marks_int_arr = [int(i) for i in marks_str_arr]#[5,4,4,2]
    d={}
    d['name']=name
    d['marks']=marks_int_arr
    newstudents.append(d)

for i in newstudents:
    name=i['name']
    marks=i['marks']
    sumi=0
    n = len(marks)
    for j in marks:
        sumi = sumi + j
    avg = sumi/n
    i['avg']=avg
#
for i in newstudents:
    if i['avg']>=mini_avg and i['avg']<=maxi_avg:
        print("YES")
    else:
        print("NO")
print(students)
print(newstudents)
print(maxi_avg,mini_avg)






# [
#     {
#         "name":"yerassyl",
#         "marks":[5,4,4,2]
#     },
#     {
#         "name":"kirito",
#         "marks":[5,4,3]
#     },
#     ...
# ]
# yerassyl __
# kirito __
# era __
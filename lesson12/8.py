from myutils import *
data=[]
n = int(input())
for i in range(n):
    line = input()
    parts = line.split(",")
    name=parts[0]
    numbers_str_arr = parts[1].split(" ")
    numbers_int_arr = list(map(int,numbers_str_arr))
    d={}
    d['name']=name
    d['avg']=find_avg(numbers_int_arr)
    d['max']=find_max(numbers_int_arr)
    data.append(d)
for i in data:
    print(i)
# 2
# yerassyl,1 2 3 4 5 
# tleugazy,5 432 1 23 
# [
#     {
#         "name":"yerassyl"
#         "avg":3,
#         "max":5,
#         "min":1
#     },
# ]
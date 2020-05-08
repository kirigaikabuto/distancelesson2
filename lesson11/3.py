# 4
# yerassyl,3/4
# kirito,20/30
# era,50/60
# anel,30/40
n = int(input())#4
students=[]
for i in range(n):
    line = input()#yerassyl,3/4
    parts = line.split(",")#['yerassyl','3/4']
    name = parts[0]#yerassyl
    mark_str = parts[1]#'3/4'
    mark_str_arr = mark_str.split("/")#['3','4']
    mark_int_arr = [int(i) for i in mark_str_arr]#[3,4]
    d={}
    d['name']=name#yerassyl
    d['mark']=mark_int_arr#[3,4]
    students.append(d)
for i in students:
    percent =(i['mark'][0]/i['mark'][1])*100
    i['mark_percent']=int(percent)
for i in students:

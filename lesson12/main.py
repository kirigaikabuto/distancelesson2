# input:
# 3
# 1,produc1,100 200 400 300,5
# 2,product2,200 350 440 370,6
# 3,product3,1 2 3 4 5,7
n = int(input())
persons=[]
for i in range(n):
    line = input()
    parts = line.split(",")
    id = parts[0]
    name = parts[1]
    arr_str = parts[2]
    number = int(parts[3])
    arr_str_arr = arr_str.split(" ")#['100','200','400','300']
    # arr_int_arr = [int(i) for i in arr_str_arr]
    arr_int_arr = list(map(int,arr_str_arr))
    d={}
    d['id']=id
    d['name']=name
    d['number']=number
    d['arr']=arr_int_arr
    persons.append(d)
for i in persons:
    arr = i['arr']
    m = len(arr)
    for j in range(m):
        arr[j]=arr[j]-i['number']

    # local_arr=[]
    # for j in arr:
    #     local_arr.append(j-i['number'])
    # i['arr']=local_arr

for i in persons:
    print(i)
# out:
# [
#     {
#         "id":1,
#         "name":product1,
#         "arr":[95,195,395,295]
#     },
#    
# ]
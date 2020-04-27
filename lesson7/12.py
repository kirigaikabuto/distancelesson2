file = open("file.txt","r")
data= file.read()
lines=data.split("\n")
n = len(lines)
arr=[]
for i in range(0,n,2):
    part1 = lines[i].split("=") #["name",""]
    part2 = lines[i+1].split('=') #["price",""]
    d={}
    d[part1[0]]=part1[1]
    d[part2[0]]=int(part2[1])
    arr.append(d)
#algorithm
for i in arr:
    print(i)
# n = len(arr)
# for i in range(n):
#     for j in range(n):
#         if arr[i]["price"]>arr[j]["price"]:
#             tmp = arr[i]
#             arr[i]=arr[j]
#             arr[j]=tmp
# for i in arr:
#     print(i)
arr=[100,122,33,45]
#[0,0,33,45]
n = len(arr)
# for i in range(n):
#     if arr[i]%2==0:
#         print(arr[i],"это четное число")
#     else:
#         print(arr[i],"это нечетное число")
for i in range(n):
    if arr[i]%2==0:
        arr[i]=0

for i in arr:
    print(i)
arr=[1,2,3,4,5]
n = len(arr)
for i in range(n):
    for j in range(n):
        if arr[i]>arr[j]:
            tmp = arr[i]
            arr[i]=arr[j]
            arr[j]=tmp
print(arr)
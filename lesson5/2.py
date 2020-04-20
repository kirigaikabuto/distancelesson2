#сортировка пузырек bubble sort
# 4 0 -1 3 4
# 0 -1 3 4 4

# 4 4 3 -1 0
# 4 0 -1 3 4
# 0 4 -1 3 4 
# 0 -1 4 3 4
# 0 -1 3 4 4

# -1 0 3 4 4
n = int(input())
arr = map(int,input().split())
arr = list(arr)
for i in range(n):
    for j in range(n):
        if arr[i]<arr[j]:
            # arr[i],arr[j]=arr[j],arr[i]
            tmp = arr[i]
            arr[i]=arr[j]
            arr[j]=tmp
print(arr)
n,maxsum = map(int,input().split())
arr = map(int,input().split())
arr = list(arr)
for i in range(n):
    for j in range(n):
        if arr[i]<arr[j]:
            tmp = arr[i]
            arr[i]=arr[j]
            arr[j]=tmp
sumi=0
count=0
for i in arr:
    if sumi+i<maxsum:
        sumi = sumi + i
        count=count+1
print(count)
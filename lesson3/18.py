arr=[1,120,31,32,4,12,321]
nechet=[]
chet=[]
n = len(arr)
for i in range(n):
    if arr[i]%2==0:
        chet.append(arr[i])
    else:
        nechet.append(arr[i])
print(arr)
print(chet)
print(nechet)
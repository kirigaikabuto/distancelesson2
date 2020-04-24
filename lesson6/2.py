n = int(input())
numbers = list(map(int,input().split()))
chet=[]
for i in range(n):
    if i%2==0:
        chet.append(numbers[i])
maxi = chet[0]
for i in chet:
    if maxi<i:
        maxi = i
print(maxi)
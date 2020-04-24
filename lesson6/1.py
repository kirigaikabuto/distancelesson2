n = int(input())
numbers = list(map(int,input().split()))
positive=[]
for i in numbers:
    if i>0:
        positive.append(i)
sumi=0
for i in positive:
    if i%2==0:
        sumi = sumi+i
print(sumi)
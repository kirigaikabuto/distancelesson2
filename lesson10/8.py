# 10 3
# arr=[1,2]
# a,b = arr
n,find = list(map(int,input().split()))
numbers=[i for i in range(1,n+1)]
numbers.remove(find)
newnumbers=[]
newnumbers.append(find)
for i in numbers:
    newnumbers.append(i)
print(newnumbers)
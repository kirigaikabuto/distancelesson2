n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
replace=[]
for i in range(m):
    eb,er = map(int,input().split())
    d={
        "element_before":eb,
        "element_replace":er
    }
    replace.append(d)
remember=[]
for i in replace:
    for j in range(len(numbers)):
        if i['element_before']==numbers[j] and (j not in remember):
            numbers[j]=i['element_replace']
            remember.append(j)
for i in numbers:
    print(i,end=" ")
#
# 7
# 1 1 5 3 1 5 1
# 2
# 5 1
# 1 3

# 5 1
# 1 1 1 3 1 1 1

# 1 3
# 3 3 3 3 3 3 3
# 1)
# вам нужно идит
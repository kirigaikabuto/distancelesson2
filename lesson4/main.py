numbers=[]
n = int(input())
for i in range(n):
    num = int(input())
    numbers.append(num)
chet=[]
nechet=[]
for i in numbers:
    if i %2==0:
        chet.append(i)
    else:
        nechet.append(i)
n_chet = len(chet)
n_nechet = len(nechet)
if n_chet>n_nechet:
    print("YES")
else:
    print("NO")
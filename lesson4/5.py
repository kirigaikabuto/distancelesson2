s = input()
#12344321
#8
#range(0,4)
#range(4,8)
n = len(s)
middle= n//2
sum1=0
sum2=0
for i in range(0,middle):
    sum1 = sum1 + int(s[i])
for i in range(middle,n):
    sum2 = sum2 + int(s[i])
if sum1 == sum2:
    print("YES")
else:
    print("NO")
a = int(input())
b = int(input())
c = int(input())
maxi = 0
mini = 0
#find max
if a>b and a>c:
    maxi=a
elif b>a and b>c:
    maxi=b
elif c>a and c>b:
    maxi=c
else:
    print("Error")
#find min
if a<b and a<c:
    mini=a
elif b<a and b<c:
    mini=b
elif c<a and c<b:
    mini=c
else:
    print("Error")
#find middle number
middle=0
if a!=maxi and a!=mini:
    middle = a
elif b!=maxi and b!=mini:
    middle = b

#check for even or odd
maxi_text ="нечетное"
mini_text ="нечетное"
if maxi%2==0:
    maxi_text = "четное"
if mini%2==0:
    mini_text = "четное"
print(mini,"это минимальное число",mini_text)
print(maxi,"это максимальное число",maxi_text)
# 30
# 40
# 51

# 40 это четное и среднее
# 30 это четное и минимальное
# 50 это нечетное и максимальное

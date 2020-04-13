a = int(input())
b = int(input())
c = int(input())
maxi = 0
if a>b and a>c:
    maxi=a
elif b>a and b>c:
    maxi=b
elif c>a and c>b:
    maxi=c
else:
    print("Error")
print(maxi)
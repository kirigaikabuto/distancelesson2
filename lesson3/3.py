arr=[120,221,330,0,1000,120]
#0->120
#1->221
#2->330
#3->0
#4->1000
n = len(arr)
sumi=0
if n==6:
    print("6 elements")
    sumi = arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]
elif n==3:
    print("3 elements")
    sumi = arr[0]+arr[1]+arr[2]
print(sumi)



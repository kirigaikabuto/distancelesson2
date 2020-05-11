#arr == a == [1,2,3,4]
def find_max(a):
    maxi = a[0]
    for i in a:
        if i>maxi:
            maxi = i
    print(maxi)


arr=[1,2,3,4]
find_max(arr)



# numbers = list(map(int,input().split()))
from myutils import *
arr=[1,2,3,4,5]
find=4
isfind = find_element(arr,find)
if isfind == 1:
    print("ok we find element")
else:
    print("Error")
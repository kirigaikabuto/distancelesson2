# надо найти максимальный элемент массива
# используя цикл for 
arr=[100,233,140,900]
maxi=arr[0]
n = len(arr)
for i in range(n):
    if maxi<arr[i]:
        maxi=arr[i]
print(maxi)
# if maxi<arr[0]:
#     maxi = arr[0]
# if maxi<arr[1]:
#     maxi = arr[1]
# if maxi<arr[2]:
#     maxi = arr[2]
# if maxi<arr[3]:
#     maxi = arr[3]
# print(maxi)
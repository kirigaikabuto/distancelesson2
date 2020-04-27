product1={
    "name":"product1",
    "price":1000
}
product2={
    "name":"product2",
    "price":2000
}
product3={
    "name":"product3",
    "price":3000
}
arr=[product1,product2,product3]
n = len(arr)
for i in range(n):
    for j in range(n):
        if arr[i]["price"]>arr[j]["price"]:
            tmp = arr[i]
            arr[i]=arr[j]
            arr[j]=tmp
for i in arr:
    print(i)
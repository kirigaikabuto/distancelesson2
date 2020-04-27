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
products=[product1,product2,product3]
sumi=0
for i in products:
    sumi = sumi +i['price']
n = len(products)
avg = sumi/n
print(f"Sum={sumi} Average Price={avg}")
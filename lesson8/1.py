import json
product1 = {
    "name":"product1",
    "price":10000
}
product2 = {
    "name":"product2",
    "price":1000
}
products=[product1,product2]
#save to file
file = open("data.json","w")
json_array = json.dumps(products,indent=4)
file.write(json_array)
file.close()
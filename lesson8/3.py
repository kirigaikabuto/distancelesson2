#read data from json file[products]
#products add new element
#save data to json file
#read data
import json
products=[]
file = open("data.json","r")
data = file.read()
products = json.loads(data)
#add element to products
name = input("write name of product:")
price = int(input("write price of product:"))
d = {
    "name":name,
    "price":price
}
products.append(d)
file.close()
#write to file
file = open("data.json","w")
json_array = json.dumps(products,indent=4)
file.write(json_array)
file.close()
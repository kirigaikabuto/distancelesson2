#read
import json
products=[]
file = open("data.json","r")
data = file.read()
products = json.loads(data)
print(products)
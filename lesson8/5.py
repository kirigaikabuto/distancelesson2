#read data from json file[products]
#products add new element
#save data to json file
#read data
import json
products=[]
file_name="person.json"
file = open(file_name,"r")
data = file.read()
products = json.loads(data)
#add element to products
username = input()
password = input()
balance  = input()
d = {
    "username":username,
    "password":password,
    'balance':balance
}
products.append(d)
file.close()
#write to file
file = open(file_name,"w")
json_array = json.dumps(products,indent=4)
file.write(json_array)
file.close()
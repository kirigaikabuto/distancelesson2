import json
users=[]
user1={
    "user_id":1,
    "email":"tleugazy98@gmail.com",
    "password":"1232323",
    "balance":12323
}
users.append(user1)
products=[]
product1 = {
    "product_id":1,
    "name":"product1",
    "price":1000
}
products.append(product1)
orders=[]
order1={
    "id_order":1,
    "id_user":1,
    "id_product":1
}
orders.append(order1)
files=["users.json","products.json","orders.json"]
data=[users,products,orders]
n = len(files)
for i in range(n):
    file_name=files[i]
    file = open(file_name,"w")
    json_array = json.dumps(data[i],indent=4)
    file.write(json_array)
    file.close()
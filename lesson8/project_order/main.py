import json
data=[]
files=["users.json","products.json","orders.json"]
n = len(files)
for i in range(n):
    file_name = files[i]
    file = open(file_name,'r')
    file_data = file.read()
    temp = json.loads(file_data)
    data.append(temp)

users,products,orders = data
#INNER JOIN

for order in orders:
    #users
    temp_user={}
    temp_product={}
    for user in users:
        if user['user_id']==order['id_user']:
            temp_user=user
    
    for product in products:
        if product['product_id']==order['id_product']:
            temp_product=product
    print(order['id_order'],temp_user['email'],temp_product['name'])
    #products
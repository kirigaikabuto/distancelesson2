teacher1 = {
    "name":"teacher1",
    "surname":"teacher1",
    "salary":10000
}
teacher2 = {
    "name":"teacher2",
    "surname":"teacher2",
    "salary":1000
}
teacher3 = {
    "name":"teacher3",
    "surname":"teacher3",
    "salary":100
}
teachers=[teacher1,teacher2,teacher3]
sumi=0
for i in teachers:
    print(i['name'],i['salary'])
    sumi = sumi + i['salary']
print(sumi)
# print(teachers[0]['name'])
# print(teacher1['name'])

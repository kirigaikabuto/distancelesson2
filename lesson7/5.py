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
maxi={}
if teacher1['salary']>teacher2['salary'] and teacher1['salary']>teacher3['salary']:
    maxi=teacher1

print(maxi)
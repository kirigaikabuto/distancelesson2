person1={
    "name":"person1",
    "age":22,
}
person2={
    "name":"person2",
    "age":20,
}
person3={
    "name":"person3",
    "age":27,
}
persons=[person1,person2,person3]
maxi = persons[0]
for person in persons:
    if maxi['age'] < person['age']:
        maxi  = person
print(maxi)

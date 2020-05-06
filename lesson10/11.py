#двумернвый массив
numbers=[]
chet_numbers=[2,4,6]
nechet_numbers=[1,3,5,3]
prime_numbers=[1,3,5]
numbers.append(chet_numbers)
numbers.append(nechet_numbers)
numbers.append(prime_numbers)
#  0  1  2    0  1  2    0  1  2
#[[2, 4, 6], [1, 3, 5], [1, 3, 5]]
#     0          1           2
# print(numbers[1][1])
counter=0
for i in numbers:
    print(i)
    for j in i:
        if j == 3:
            counter = counter +1
print(counter)

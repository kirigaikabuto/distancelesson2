words = input().split()
numbers=[]
others=[]
for i in words:
    if i.isdigit():
        numbers.append(i)
    else:
        others.append(i)
print(numbers)
print(others)
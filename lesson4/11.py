s = "Hello from 1994 dsd!"
words = s.split(" ")
numbers=[]
alpha=[]
others=[]
for i in words:
    if i.isdigit():
        num = int(i)
        numbers.append(num)
    if i.isalpha():
        alpha.append(i)
    if not i.isdigit() and not i.isalpha():
        others.append(i)
print(numbers)
print(alpha)
print(others)
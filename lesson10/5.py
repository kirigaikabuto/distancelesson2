s="1 2 3 4 5 6 7 8 9"
words=s.split()
numbers=[]
for i in words:
    num = int(i)
    numbers.append(num)
print(numbers)
sumi=0
for i in numbers:
    sumi = sumi + i
print(sumi)
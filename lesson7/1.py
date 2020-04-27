file = open("input.txt","r")
data = file.read()
words = data.split("\n")
numbers = []
for i in words:
    numbers.append(int(i))
maxi=numbers[0]
for i in numbers:
    if maxi<i:
        maxi=i
out = open("output.txt","w")
out.write(str(maxi))
file.close()
out.close()
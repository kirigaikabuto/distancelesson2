file = open("file.txt","r")
data = file.read()
parts = data.split("\n")
n = len(parts)
for i in range(0,n,2):
    print(parts[i],parts[i+1])
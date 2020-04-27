file = open("file.txt","r")#r-read
data = file.read()
words = data.split("\n")
words = words[:len(words)-1]
print(words)
file.close()
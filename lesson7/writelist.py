file = open("file.txt","w")#w-write
arr=["hello","world","adssd"]
print(arr[0])
for i in arr:
    word = i + "\n"
    file.write(word)
file.close()
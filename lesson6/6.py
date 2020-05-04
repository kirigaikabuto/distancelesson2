s="Hello world badadd Yerassyl"
words=s.split()
lengths=[]
for i in words:
    lengths.append(len(i))
n = len(lengths)
maxi=lengths[0]
maxi_index=0
for i in range(n):
    if maxi<lengths[i]:
        maxi = lengths[i]
        maxi_index=i
word = words[maxi_index]
print(word,maxi)
#разбить все по словам 
#создать второй массив в котором мы будем хранить длинны наших слова
#эквивалентно массив из слова
#["Hello","world"...]
#[5,5]
#Yerassyl 8
s="Привет меня зовут Ерасыл мне 22.Я живу в городе Алматы.Алматы построили в 18 веке"
# 1) делим по точкам ["Привет Привет зовут Ерасыл мне 22","Я живу в городе Алматы","Алматы построили в 18 веке"]
# 2) делим по пробелам одновременно все закидывать в общий массив
# 3) ['Привет','Привет'....'живу']
# 4) разбирать на числа и слова
preds = s.split(".")
words=[]
for i in preds:
    preds_words = i.split(" ")
    words=words+preds_words
numbers=[]
slova=[]
for i in words:
    if i.isalpha():
        slova.append(i)
    elif i.isdigit():
        numbers.append(i)
print(numbers)
print(slova)
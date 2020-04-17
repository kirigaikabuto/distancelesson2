phrase = "Привет, меня зовут Тимур, мне 25. Я живу в г. Алматы, построенном в 19 веке"
phrase = phrase.split(".")
phrase_elements = []
words = []
numbers = []
for p in phrase:
    phrase_elements.append(p.split(" "))

for p in phrase_elements:
    for i in range(len(p)):
        if p[i].isdigit():
            numbers.append(p[i])
        else: 
            words.append(p[i])

print(numbers)
print(words)
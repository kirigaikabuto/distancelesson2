# 12 232 434 56 123 343 1 0
# one_arr=[]#цифра с 1 элементов 0 1 2 3 4 5 6 7 8 9
# two_arr =[]#двухзначные 10 11 12 31
# three_arr=[]#трехзначные
s = input()
words = s.split(" ")
one_arr=[]
two_arr=[]
three_arr=[]
for i in words:
    n = len(i)
    if n==1:
        one_arr.append(i)
    elif n==2:
        two_arr.append(i)
    elif n==3:
        three_arr.append(i)
s = "Мои числа {} {}"
onestr = " ".join(one_arr)
onestr = s.format("однозначные",onestr)
twostr = " ".join(two_arr)
twostr = s.format("двухзначные",twostr)
print(onestr)
print(twostr)
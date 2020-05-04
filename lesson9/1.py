#10 5
n,find = map(int,input().split())
numbers=[]
for i in range(1,n+1):
    numbers.append(i)

1)найти элемент и его индекс(index)
2)newnumbers=numbers[:index]
#numbers=[1 2 3 4 5 6 7 8 9 10]
#newnumbers=[]
#добавить изначально то число которое мы искали [5]
#newnumbers поместить элементы до 5 и после 5 numbers[:index] number[index+1:]
# numbers[:index] ->1 2 3 4
#number[index+1:] 6 7 8 9 10
#нужно сложить все массивы и конечный итог вывести
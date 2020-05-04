n = int(input())
points=[]
for i in range(n):
    x,y = map(int,input().split())
    point={
        "x":x,
        "y":y
    }
    points.append(point)
calculations=[]
в массив calculations добавить вычисление расстойний от каждой дочи до другой точки
а затем вывести все значения из массива calculations по 1 экзэмпляру без повторений
# 4
# 0 0
# 1 1
# 1 0
# 0 1

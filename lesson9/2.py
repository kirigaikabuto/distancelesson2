n = int(input())
hosts=[]
for i in range(n):
    host = input()
    x,y,r = map(int,input().split())
    d={
        "name":host,
        "x":x,
        "y":y,
        "r":r
    }
    hosts.append(d)

x,y = map(int,input().split())
for i in hosts:
    print(i)
#1) найти используя формула нахождения расстояние между точками расстояние
от точки  x,y до каждого host 
#2) сравнивать расстояние которые вы нашли с радиусом этого хоста
и если расстояние меньше чем радиус вывести название хоста
# 8
# 1 2 3 4 5 6 7 8 
# 5
# Ответ(6+7+8)
# 21
n = int(input())
numbers=list(map(int,input().split()))
find = int(input())
find_index=0
for i in range(n):
    if numbers[i] == find:
        find_index = i
final_arr = numbers[find_index+1:]
sumi=0
for i in final_arr:
    sumi = sumi + i
print(sumi)
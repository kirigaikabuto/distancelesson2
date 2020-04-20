n = int(input())
numbers=list(map(int,input().split()))
start,end = map(int,input().split())
numbers_part1 = numbers[:start]
numbers_part2 = numbers[end+1:]
total = numbers_part1+numbers_part2
print(total)
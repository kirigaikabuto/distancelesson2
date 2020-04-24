n = int(input())
numbers = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if numbers[i]<numbers[j]:
            tmp = numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=tmp
max_counter=0
max_value=0
current_counter=1
for i in range(n-1):
    if numbers[i]==numbers[i+1]:
        current_counter+=1
    else:
        if current_counter>max_counter:
            max_counter = current_counter
            max_value = numbers[i]
        current_counter=1
print(f"{max_value} repeated {max_counter} times")

    
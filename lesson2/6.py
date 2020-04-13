# 0<=summa<50000 1.3
# 50000<=summa<100000 1.6 
# 100000<=summa<150000 1.9
summa = int(input())
percent=0.0
if summa>=0 and summa<50000:
    percent = 1.3
elif summa>=50000 and summa<100000:
    percent = 1.6 
elif summa>=100000 and summa<150000:
    percent = 1.9
else:
    print("Error")
total_sum = summa+summa*percent/100
print(total_sum)
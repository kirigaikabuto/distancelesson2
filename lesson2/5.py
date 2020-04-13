summa = int(input())
percent = 0.0
#условия
if summa<50000:
    percent = 1.3
elif summa<100000:
    percent = 2.1
else:
    percent = 3.0
#конец условия
total_sum = summa+summa*percent/100
print(total_sum)
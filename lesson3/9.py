salary=[1000,2000,3000,500]
for i in salary:
    if i>=800:
        percent = i*0.3
    else:
        percent = i*0.5
    total = i+percent
    print(total)
    
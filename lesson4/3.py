s = "python"
print(s)
s = list(s)
s[0]="T"
s[2]="p"
total=""
for i in s:
    total= total+i
print(total)
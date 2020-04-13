a = int(input())
b = int(input())
c = int(input())
avg = (a+b+c)/3
#a
a_text=""
if a>avg:
    a_text=">"
elif a<avg:
    a_text="<"
else:
    a_text="="
#b
b_text=""
if b>avg:
    b_text=">"
elif b<avg:
    b_text="<"
else:
    b_text="="
#c
c_text=""
if c>avg:
    c_text=">"
elif c<avg:
    c_text="<"
else:
    c_text="="
print(a,a_text)
print(b,b_text)
print(c,c_text)
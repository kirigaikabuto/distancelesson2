number1 = int(input("Write first number:"))
number2 = int(input("Write second number:"))
znak = input("Write operation:")
total=0
if znak=="+":
    total = number1+number2 
elif znak == "/":
    total = number1/number2
elif znak == "-":
    total = number1-number2
elif znak == "*":
    total = number1*number2
else:
    print("Error")
print(total)
# 3    3    50   
# 4    4    5
# +    *    /

# 7    12   10
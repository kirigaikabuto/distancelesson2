n = int(input())
numbers=map(int,input().split())
numbers = list(numbers)
maxsequence=0
sequence=0
for i in numbers:
    if sequence>maxsequence:
        maxsequence = sequence
    if i>0:
        sequence+=1
    else:
        sequence=0
    st = f"Current Sequence {sequence},Max Sequence {maxsequence},Current number is {i}"
    print(st)
print(maxsequence)

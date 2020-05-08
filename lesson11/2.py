# A - 90-100
# B - 80-90
# C - 70-80
# D - 60-70
# E - 50-60
d={}
d['A']=[i for i in range(90,101)]
#code
for i in d:
    if 75 in d[i]:
        print(i)#C
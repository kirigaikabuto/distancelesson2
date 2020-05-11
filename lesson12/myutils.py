def find_max(a):
    maxi = a[0]
    for i in a:
        if i>maxi:
            maxi = i
    return maxi
def find_sumi(b):
    sumi = 0 
    for i in b:
        sumi = sumi +i
    return sumi
def find_avg(c):
    sumi = find_sumi(c)
    return sumi/len(c)
def getAge(dictionary):
    return 2020-dictionary['year']

def find_element(array,element):
    isfind=0
    for i in array:
        if i == element:
            isfind = 1
    return isfind
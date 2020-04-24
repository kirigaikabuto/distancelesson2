n = int(input())
numbers = list(map(int,input().split()))
maxi =numbers[0]
maxi_index=0
mini =numbers[0]
mini_index=0
for i in range(n):
    if maxi<numbers[i]:
        maxi=numbers[i]
        maxi_index=i
    if mini>numbers[i]:
        mini=numbers[i]
        maxi_index=i
start = mini_index
end = maxi_index
if maxi_index<mini_index:
    start = maxi_index
    end = mini_index
sumi=0
for i in range(start+1,end):

# 8
# 1 2 3 8 4 5 6 0
#       3       7  
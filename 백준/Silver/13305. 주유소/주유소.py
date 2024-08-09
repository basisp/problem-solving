import sys
input=sys.stdin.readline
N=int(input())
Distance=list(map(int,input().split()))
Price=list(map(int,input().split()))
Price.pop()

total=0

for i in range(1,N-1):
    if Price[i]>Price[i-1]:
        Price[i]=Price[i-1]

for i in range(N-1):
    total+=Price[i]*Distance[i]

print(total) 





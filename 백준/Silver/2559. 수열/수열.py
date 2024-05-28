import sys
from collections import deque

N,K=map(int,input().split())

S=list(map(int,sys.stdin.readline().split()))


sum=0
L=[0]

for i in S:
    sum+=i
    L.append(sum)

T=[]
for i in range(K,N+1):
    T.append(L[i]-L[i-K])

print(max(T))

import sys
from collections import deque

N,M=map(int,input().split())

S=list(map(int,sys.stdin.readline().split()))

for i in range(1,len(S)):
    S[i]=S[i]+S[i-1]

def prefixsum(S,i,j):
    if i==1:
        return S[j-1]
    else:
        return S[j-1]-S[i-2]



for _ in range(M):
    i,j=map(int,sys.stdin.readline().split())
    print(prefixsum(S,i,j))




import sys

N=int(input())

S=[]
for _ in range(N):
    k=list(map(int,input().split()))
    k.reverse()
    S.append(k)

S.sort()

for element in S:
    print(element[1],element[0],sep=' ')
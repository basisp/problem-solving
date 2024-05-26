import sys

N=int(input())

S=[]
for _ in range(N):
    S.append(tuple(map(int,input().split())))

S.sort()

for element in S:
    print(element[0],element[1],sep=' ')
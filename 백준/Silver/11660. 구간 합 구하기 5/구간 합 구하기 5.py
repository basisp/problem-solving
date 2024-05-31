import sys

N,M=map(int,input().split())

S=[]

for _ in range(N):
    S.append(list(map(int,sys.stdin.readline().split())))

prefixsum=[[0]*(N+1) for _ in range(N+1)]

for l in range(1,N+1):
    for j in range(1,N+1):
        prefixsum[l][j]=prefixsum[l-1][j]+prefixsum[l][j-1]-prefixsum[l-1][j-1]+S[l-1][j-1]


def partsum(stack):
    return prefixsum[stack[2]][stack[3]]-prefixsum[stack[0]-1][stack[3]]-prefixsum[stack[2]][stack[1]-1]+prefixsum[stack[0]-1][stack[1]-1]


for _ in range(M):
    stack=list(map(int, sys.stdin.readline().split()))
    print(partsum(stack))
    
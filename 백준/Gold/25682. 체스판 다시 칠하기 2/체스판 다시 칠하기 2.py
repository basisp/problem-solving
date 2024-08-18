import sys

n,m,k=map(int,sys.stdin.readline().split())

temp=[]
for _ in range(n):
    temp.append(sys.stdin.readline().rstrip())

arr=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if temp[i][j]=='B':
            arr[i][j]=1

dpB=[[0]*m for _ in range(n)]
dpW=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            dpB[i][j]=1
        else:
            dpW[i][j]=1

#바꿔줘야 할 부분 1 아닌 부분 0

arr_dpW=[[0]*(m+1) for _ in range(n+1)]
arr_dpB=[[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if arr[i][j]!=dpW[i][j]:
            arr_dpW[i+1][j+1]=1
        if arr[i][j]!=dpB[i][j]:
            arr_dpB[i+1][j+1]=1

#누적합

for i in range(1,n+1):
    for j in range(1,m+1):
        arr_dpB[i][j]+=arr_dpB[i][j-1] + arr_dpB[i-1][j]-arr_dpB[i-1][j-1]
        arr_dpW[i][j]+=arr_dpW[i][j-1] + arr_dpW[i-1][j]-arr_dpW[i-1][j-1]

#k*k 에서 누적합의 최소 구하기 (이차원에서의 누적합)
import math
min_v=math.inf
for i in range(k,n+1):
    for j in range(k,m+1):
        min_v=min(min_v, arr_dpB[i][j]-arr_dpB[i][j-k]-arr_dpB[i-k][j]+arr_dpB[i-k][j-k],arr_dpW[i][j]-arr_dpW[i][j-k]-arr_dpW[i-k][j]+arr_dpW[i-k][j-k])



print(min_v)

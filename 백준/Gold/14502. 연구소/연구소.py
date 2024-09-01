import sys

n,m=map(int,sys.stdin.readline().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

directions=[(0,1),(0,-1),(1,0),(-1,0)]
from collections import deque
from itertools import combinations

def bfs(arr):
    Q=deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j]==2:
                Q.append([i,j])

    while Q:
        a,b=Q.popleft()
        for di,dj in directions:
            ni=a+di; nj=b+dj
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0:
                arr[ni][nj]=2
                Q.append([ni,nj])
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                cnt+=1

    return cnt

import copy
res=[]
comb=[(i,j) for i in range(n) for j in range(m)]
for list in combinations(comb,3):
    arr_v=copy.deepcopy(arr)
    valid=True
    for a,b in list:
        if arr[a][b]!=0:
            valid=False
            break
        else:
            arr_v[a][b]=1
    if valid:
        res.append(bfs(arr_v))

print(max(res))
    



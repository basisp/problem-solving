# 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
#  단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
#한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 그림 1의 빙산에 대해서는 2가 답이다. 
# 만일 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력한다.

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

year=0
ice=1
directions=[(0,1),(0,-1),(1,0),(-1,0)]

def dfs(i,j,k):

    for di,dj in directions:
        ni=i+di; nj=j+dj
        if 0<=ni<n and 0<=nj<m and visited[ni][nj]==0 and arr[ni][nj]!=0:
            visited[ni][nj]=k
            dfs(ni,nj,k)

    return k+1
    
            

import copy
year=0
while True:
    arr1=copy.deepcopy(arr)
    year+=1
    for i in range(n):
        for j in range(m):
            for di,dj in directions:
                ni=i+di; nj=j+dj
                if 0<=ni<n and 0<=nj<m and arr[ni][nj]==0 and arr1[i][j]-1>=0:
                    arr1[i][j]-=1
    arr=arr1
    visited=[[0]*m for _ in range(n)]
    k=1
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 and visited[i][j]==0 and k<=2:
                visited[i][j]=k
                k=dfs(i,j,k)
    if k>=3:
        print(year)
        break

    sum_v=0
    for ele in visited:
        sum_v+=sum(ele)
    if sum_v==0:
        print(0)
        break
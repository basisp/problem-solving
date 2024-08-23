import sys
from collections import deque
input=sys.stdin.readline
n,m,t=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

#3차원
Q=deque([[0,0,0]])
direction=[(0,1),(0,-1),(1,0),(-1,0)]
visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0]=1

while Q:
    i,j,k=Q.popleft()
    if i==n-1 and j==m-1 and visited[i][j][k]-1<=t:
        print(visited[i][j][k]-1)
        sys.exit(0)

    if k==0:
        for di,dj in direction:
            ni=i+di; nj=j+dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj][k]==0 and graph[ni][nj]==0:
                visited[ni][nj][k]=visited[i][j][k]+1
                Q.append([ni,nj,k])
            elif 0<=ni<n and 0<=nj<m and visited[ni][nj][k]==0 and graph[ni][nj]==2:
                visited[ni][nj][k+1]=visited[i][j][k]+1
                visited[ni][nj][k]=visited[i][j][k]+1
                Q.append([ni,nj,k+1])
    
    elif k==1:
        for di,dj in direction:
            ni=i+di; nj=j+dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj][k]==0:
                visited[ni][nj][k]=visited[i][j][k]+1
                Q.append([ni,nj,k])        

print('Fail')

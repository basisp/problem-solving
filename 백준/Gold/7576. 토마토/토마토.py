
import sys
from collections import deque

m,n=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

directions=[(0,1),(0,-1),(1,0),(-1,0)]
t=0
Q=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            Q.append([i,j])
if len(Q)==n*m:
    print(0)
    quit()

def bfs():
    
    while Q:
        i,j=Q.popleft()
        
        for di,dj in directions:
            ni=i+di; nj=j+dj
            if 0<=ni<n and 0<=nj<m and graph[ni][nj]==0:
                graph[ni][nj]=graph[i][j]+1
                Q.append([ni,nj])
bfs()
max_v=0
for i in range(n):
    for j in range(m):
        if max_v<graph[i][j]:
            max_v=graph[i][j]
        if graph[i][j]==0:
            print(-1)
            quit()
        
print(max_v-1)

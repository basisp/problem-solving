import sys
from collections import deque

M, N,H = map(int, sys.stdin.readline().split())

build= [[list(map(int,sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

visited=[[[-1]*M for _ in range(N)] for _ in range(H)]




def search():

    Q=deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if build[i][j][k]==1:
                    visited[i][j][k]=0
                    Q.append((i,j,k))
                elif build[i][j][k]==-1:
                    visited[i][j][k]=-2
                   

    while Q:
        i,j,k=Q.popleft()
        for di,dj,dk in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            ti,tj,tk=i+di,j+dj,k+dk
            if 0<=ti<=H-1 and 0<=tj<=N-1 and 0<=tk<=M-1 and visited[ti][tj][tk]==-1:    
                visited[ti][tj][tk]=visited[i][j][k]+1
                Q.append((ti,tj,tk))

    res=0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k]==-1:
                    return -1
                res=max(visited[i][j][k],res)
    
    
    return res

result=search()
print(result)

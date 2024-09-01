from collections import deque

res=[]
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    
    return bfs(maps,n,m)
        
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(maps,n,m):
    global directions,res
    visited=[[0]*m for _ in range(n)]
    Q=deque([[0,0]])
    visited[0][0]=1
    while Q:
        i,j = Q.popleft()
        
        if visited[n-1][m-1]:
            return visited[n-1][m-1]
    
        for di,dj in directions:
            ni=di+i; nj=dj+j
            if 0<=ni<n and 0<=nj<m and maps[ni][nj]==1 and visited[ni][nj]==0:
                visited[ni][nj]=visited[i][j]+1
                Q.append([ni,nj])        
                
    return -1
    
    
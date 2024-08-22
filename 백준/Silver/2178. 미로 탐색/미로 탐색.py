import sys

n,m=map(int,sys.stdin.readline().split())

graph=[]

for _ in range(n):
    graph.append([int(x) for x in sys.stdin.readline().strip()])


from collections import deque
directions=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(V):
    visited=[[0]*m for _ in range(n)]
    if graph[0][0]==1:
        visited[0][0]=1
        Q=deque([V])

        while Q:
            x,y=Q.popleft()
            for dx,dy in directions:
                nx=x+dx; ny=y+dy
                if 0<=nx<=n-1 and 0<=ny<=m-1 and visited[nx][ny]==0 and graph[nx][ny]==1:
                    visited[nx][ny]=visited[x][y]+1
                    Q.append([nx,ny])
    
    return visited
    
print(bfs([0,0])[n-1][m-1])
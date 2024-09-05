def solution(rectangle, characterX, characterY, itemX, itemY):
    characterX*=2; characterY*=2 ; itemX*=2; itemY*=2
    graph=[[0]*102 for _ in range(102)]
    
    for ele in rectangle:
        a,b,c,d=ele 
        a*=2;b*=2;c*=2;d*=2
        
        for i in range(a+1,c):
            for j in range(b+1,d):
                graph[j][i]=2
        
        for i in range(a,c+1):
            if graph[b][i]!=2:
                graph[b][i]=1
            if graph[d][i]!=2:
                graph[d][i]=1
        for j in range(b,d+1):
            if graph[j][a]!=2:
                graph[j][a]=1
            if graph[j][c]!=2:        
                graph[j][c]=1
    visited=[[0]*102 for _ in range(102)]
    visited[characterY][characterX]=1
    visited=bfs(graph,characterX,characterY,visited,itemX, itemY)
    return (visited[itemY][itemX]-1)//2

directions=[(0,1),(0,-1),(1,0),(-1,0)]

from collections import deque
def bfs(graph,characterX, characterY,visited,itemX, itemY):
    Q=deque([[characterX, characterY]])

    while Q:
        x,y=Q.popleft()
        if x==itemX and y==itemY:
            break
        
        for dx,dy in directions:
            nx=x+dx; ny=y+dy
            if 0<=nx<102 and 0<=ny<102 and visited[ny][nx]==0 and graph[ny][nx]==1:
                visited[ny][nx]=visited[y][x]+1
                Q.append([nx,ny])
                
    return visited
            
        
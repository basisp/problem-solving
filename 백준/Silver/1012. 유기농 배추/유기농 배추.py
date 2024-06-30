import sys

T=int(input())

def dfs(y,x):
    if x<0 or x>=M or y<0 or y>=N or land[y][x] ==0 or visited[y][x]:
        return 0
    count=1
    visited[y][x]=1

    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx,ny=x+dx,y+dy
        count+=dfs(ny,nx)

    return count

for _ in range(T):
    M, N, K =map(int, sys.stdin.readline().split())
    land=[[0]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,sys.stdin.readline().split())
        land[y][x]=1
    visited=[[0]*M for _ in range(N)]
    res=[]
    for y in range(N):
        for x in range(M):
            n=dfs(y,x)
            if n!=0:
                res.append(n)

    print(len(res))

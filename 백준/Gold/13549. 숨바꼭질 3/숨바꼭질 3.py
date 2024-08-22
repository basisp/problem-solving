import sys
from collections import deque
input=sys.stdin.readline
n,k=map(int,input().split())
limit=100000
visited=[-1]*(limit+1)
direction=[-1,1]
def dfs(n):
    Q=deque([n])
    visited[n]=0
    while Q:
        num=Q.popleft()

        tp=num*2
        while tp<=limit and visited[tp]==-1:
            visited[tp]=visited[num]
            Q.append(tp)
            tp*=2

        for dx in direction:
            nx=num+dx
            if 0<=nx<=limit and visited[nx]==-1:
                visited[nx]=visited[num]+1
                Q.append(nx)

dfs(n)
print(visited[k])
        
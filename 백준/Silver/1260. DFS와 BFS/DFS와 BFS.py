import sys 
input=sys.stdin.readline
n,m,v=map(int,input().split())

E=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)
    
for k in range(n+1):
    E[k].sort()

visited=[0]*(n+1)
res=[]

def dfs(v): # -> 재귀 o
    if visited[v]==0:
        visited[v]=1
        res.append(v)
        for ele in E[v]:
            dfs(ele)

dfs(v)
print(' '.join(map(str,res)))



visited=[0]*(n+1)
res.clear()
from collections import deque
Q=deque()

def bfs(v): #-> 재귀 x , 큐, while
    visited[v]=1
    Q.append(v)
    while Q:
        t= Q.popleft()
        res.append(t)
        for ele in E[t]:
            if not visited[ele]:
                visited[ele]=1
                Q.append(ele)

bfs(v)
print(' '.join(map(str,res)))

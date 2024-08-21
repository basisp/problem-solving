import sys
input=sys.stdin.readline

n,m,V=map(int,input().split())


graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for ele in graph:
    ele.sort(reverse=True)

def dfs(V):
    visited=[0]*(n+1)
    res=[]
    stack=[V]
    while stack:
        num=stack.pop()
        if visited[num]==0:
            visited[num]=1
            res.append(num)
            for i in range(len(graph[num])):
                if visited[graph[num][i]]==0:
                    stack.append(graph[num][i])
    print(' '.join(map(str,res)))

dfs(V)

from collections import deque

def bfs(V):
    visited=[0]*(n+1)
    res=[]
    Q=deque([V])
    while Q:
        num=Q.popleft()
        if visited[num]==0:
            visited[num]=1
            res.append(num)
            for i in range(len(graph[num])-1,-1,-1):
                if visited[graph[num][i]]==0:
                    Q.append(graph[num][i])
    print(' '.join(map(str,res)))

bfs(V)

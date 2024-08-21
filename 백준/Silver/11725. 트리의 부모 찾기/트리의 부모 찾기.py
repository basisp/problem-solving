import sys

input=sys.stdin.readline

n=int(input())
graph=[ [] for _ in range(n+1)]
for _ in range(n-1):
    a,b =map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for ele in graph:
    ele.sort()

cnt=1
visited=[0]*(n+1)
from collections import deque
Q=deque([1])

while Q:
    num=Q.popleft()
    if visited[num]==0:
        visited[num]=cnt
        cnt+=1
        for ele in graph[num]:
            if visited[ele]==0:
                Q.append(ele)

for i in range(2,n+1):
    ans=1e7
    for ele in graph[i]:
        ans=min(ans,visited[ele])
    for ele in graph[i]:
        if visited[ele]==ans:
            print(ele)

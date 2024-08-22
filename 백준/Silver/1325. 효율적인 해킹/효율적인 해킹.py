import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)

from collections import defaultdict

res=defaultdict(list)
def solve(V):
    Q=deque([V])
    visited=[0]*(n+1)
    cnt=0
    while Q:
        node=Q.popleft()
        if visited[node]==0:
            visited[node]=1
            cnt+=1
            for ele in graph[node]:
                if visited[ele]==0:
                    Q.append(ele)
    res[V].append(cnt)
for i in range(1,n+1):
    solve(i)
    

ans=[]
t=max(res.values())
for key,value in res.items():
    if value==t:
        ans.append(key)


print(*ans)
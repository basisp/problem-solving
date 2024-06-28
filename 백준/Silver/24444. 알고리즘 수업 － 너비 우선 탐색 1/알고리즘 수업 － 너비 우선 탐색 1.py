import sys
from collections import deque
N,M,R = map(int, sys.stdin.readline().split())

E=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    E[a].append(b)
    E[b].append(a)

for l in range(N+1):
    E[l].sort()

visited=[0]*(N+1)

Q=deque()
def bfs(E,R):
    count=1
    visited[R]=count
    count+=1
    Q.append(R)
    while Q:
        u=Q.popleft()
        for element in E[u]:
            if visited[element]==0:
                visited[element]=count
                count+=1
                Q.append(element)

bfs(E,R)
for visit in visited[1:]:
    print(visit)



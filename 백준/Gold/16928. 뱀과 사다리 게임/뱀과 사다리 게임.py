import sys
from collections import deque

S, B = map(int, sys.stdin.readline().split())

visited = [-1]*100
info = list(range(100))

for _ in range(S+B):
    x,y = map(int,sys.stdin.readline().split())
    info[x-1]=(y-1)

Q=deque([0])
visited[0]=0

while Q:
    n=Q.popleft()

    if n==99:
        break

    for dn in range(1,7):
        tn=n+dn
        if 0<=tn<=99:
            final_pos=info[tn]
            if visited[final_pos]==-1 or visited[final_pos]>visited[n]+1:
                visited[final_pos]=visited[n]+1
                Q.append(final_pos)

print(visited[99])


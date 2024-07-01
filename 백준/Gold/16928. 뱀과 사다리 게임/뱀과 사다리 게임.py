import sys
from collections import deque

S, B = map(int, sys.stdin.readline().split())

visited = [-1]*100
info = [0 for _ in range(100)]

Q=deque()

for _ in range(S+B):
    x,y = map(int,sys.stdin.readline().split())
    info[x-1]=(y-1)

Q.append(0)

visited[0]=0


while Q:
    n=Q.popleft()
    if info[n]!=0:
        if visited[info[n]]==-1:
            visited[info[n]]=visited[n]
            Q.append(info[n])
        else:
            visited[info[n]]=min(visited[info[n]],visited[n])
            Q.append(info[n])

    elif info[n]==0:
        for dn in range(1,7):
            tn=n+dn
            if 0<=tn<=99:
                if visited[tn]==-1:
                    visited[tn]=visited[n]+1
                    Q.append(tn)
                elif visited[tn]!=-1:
                    if visited[tn]<=visited[n]+1:
                        continue
                    else:
                        visited[tn]=min(visited[n]+1,visited[tn])
                        Q.append(tn)

print(visited[99])


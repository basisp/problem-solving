import sys
from collections import deque

n = int(input())
Q = deque()
for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0]=="push":
        Q.append(cmd[1])
    if cmd[0]=="pop":
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    if cmd[0]=="size":
        print(len(Q))
    if cmd[0]=="empty":
        if Q:
            print(0)
        else:
            print(1)
    if cmd[0]=="front":
        if Q:
            print(Q[0])
        else:
            print(-1)
    if cmd[0]=="back":
        if Q:
            print(Q[-1])
        else:
            print(-1)
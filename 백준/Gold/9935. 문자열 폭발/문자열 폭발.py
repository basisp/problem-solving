import sys
from collections import deque

Q = deque(list(sys.stdin.readline().rstrip()))
bomb = list(sys.stdin.readline().rstrip())

L = []

while Q:
    L.append(Q.popleft())
    if len(L) >= len(bomb) and L[-1] == bomb[-1]:
        match = True
        for i in range(1, len(bomb)):
            if L[-1 - i] != bomb[-1 - i]:
                match = False
                break
        if match:
            for _ in range(len(bomb)):
                L.pop()

if len(L) == 0:
    print('FRULA')
else:
    print(''.join(L))

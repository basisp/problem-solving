import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
max_v = 100000
visited = [-1] * (max_v + 1)
directions = [-1, 1]

def bfs(n):
    Q = deque([n])
    visited[n] = 0
    
    while Q:
        num = Q.popleft()
        
        # 순간이동 먼저 처리
        tp = num * 2
        while tp <= max_v and visited[tp] == -1:
            visited[tp] = visited[num]
            Q.append(tp)
            tp *= 2
        
        # 걷기 처리
        for dx in directions:
            nx = num + dx
            if 0 <= nx <= max_v and visited[nx] == -1:
                visited[nx] = visited[num] + 1
                Q.append(nx)

bfs(n)
print(visited[k])

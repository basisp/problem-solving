import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

Q = deque()
visited = [-1] * 100001 

def search(N, K):
    visited[N] = 0
    Q.append(N)
    
    while Q:
        n = Q.popleft()
        
        if n == K:  
            return visited[n]
        
        for nx in [n-1, n+1, 2*n]:
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = visited[n] + 1
                Q.append(nx)
    
    return -1  

result = search(N, K)

print(result)
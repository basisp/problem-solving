import sys
from collections import deque

input = sys.stdin.readline
limit_K = int(input())

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 3차원 visited 배열: [i][j][k] - 말의 이동 횟수 k에 따라 따로 방문 처리
visited = [[[-1] * (limit_K + 1) for _ in range(m)] for _ in range(n)]
Q = deque([[0, 0, 0]])
visited[0][0][0] = 0

# 말 이동 방향
k_directions = [(-2, 1), (-2, -1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
# 일반 이동 방향
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while Q:
    i, j, k = Q.popleft()

    if i == n-1 and j == m-1:
        print(visited[i][j][k])
        sys.exit(0)

    if k < limit_K:
        for di, dj in k_directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0 and visited[ni][nj][k+1] == -1:
                visited[ni][nj][k+1] = visited[i][j][k] + 1
                Q.append([ni, nj, k+1])

    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] == 0 and visited[ni][nj][k] == -1:
            visited[ni][nj][k] = visited[i][j][k] + 1
            Q.append([ni, nj, k])

print(-1)

from collections import deque
#인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴된다. 따라서, 연쇄 반응은 없다.

import sys

R, C, N=map(int,sys.stdin.readline().split())

graph=[]

for i in range(R):
    graph.append(list(input().rstrip()))

directions=[(0,1),(0,-1),(1,0),(-1,0)]

#폭탄 폭발
Q=deque()
def dfs(Q,graph):
    while Q:
        x,y=Q.popleft()
        graph[x][y]='.'
        for dx,dy in directions:
            nx=x+dx; ny=y+dy
            if 0<=nx<R and 0<=ny<C:
                graph[nx][ny]='.'

#시간에 따른 과정
def simulate(t):
    global Q,graph
    if t==1:
        for i in range(R):
            for j in range(C):
                if graph[i][j]=='O':
                    Q.append([i,j])

    elif t%2==1: #3 5 7
        dfs(Q,graph)
        for i in range(R):
            for j in range(C):
                if graph[i][j]=='O':
                    Q.append([i,j])

    else:
        graph=[['O']*C for _ in range(R)]

for i in range(1,N+1):
    simulate(i)

for i in range(R):
    print(''.join(graph[i]))

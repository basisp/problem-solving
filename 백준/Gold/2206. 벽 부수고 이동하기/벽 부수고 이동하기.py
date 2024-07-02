import sys
from collections import deque
import copy

#한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
#벽을 한 개 까지 부수고 이동하여도 된다.

N,M=map(int,sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

v = [[[0, 0] for _ in range(M)] for _ in range(N)]

def search():
    Q=deque([(0,0,0)])
    v[0][0][0]=1
   
    while Q:
        x,y,z = Q.popleft()
        if x==N-1 and y==M-1:
            return v[x][y][z]
        
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            tx,ty=dx+x,dy+y
            if 0<=tx<N and 0<=ty<M:
                if land[tx][ty]==0 and v[tx][ty][z]==0: 
                    v[tx][ty][z]=v[x][y][z]+1
                    Q.append((tx,ty,z))
                elif land[tx][ty]== 1 and z==0:
                    v[tx][ty][1]=v[x][y][z]+1
                    Q.append((tx,ty,1))
    return -1

result = search()
print(result if result != -1 else -1)
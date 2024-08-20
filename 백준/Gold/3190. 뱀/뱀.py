#머리부터 들어감

import sys
input=sys.stdin.readline
n=int(input())
k=int(input())
#사과의 위치
k_arr=[]
for _ in range(k):
    k_arr.append(list(map(int,input().split())))
#뱀의 방향 전환 횟수
L=int(input())
L_arr=[]
for _ in range(L):
    L_arr.append(input().split())

dp=[[0]*(n+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=1
for a,b in k_arr:
    dp[a][b]=5

cnt=0
i=j=1
from collections import deque
Q=deque([[1,1]]) #***********************************************
dp[1][1]=0
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 순서대로: 우, 하, 좌, 상
current_dir = 0  # 현재 방향: 0 = 우, 1 = 하, 2 = 좌, 3 = 상
k=0;l=1
while True:
    cnt+=1
    i+=k
    j+=l
    if dp[i][j]==0:
        break

    Q.append([i,j])
    dp[i][j]=0
    if [i,j] in k_arr:
        k_arr.remove([i,j])
    else:
        y,u=Q.popleft()
        dp[y][u]=1

    for ele in L_arr:
        if int(ele[0]) == cnt:
            if ele[1] == 'L':
                current_dir = (current_dir - 1) % 4  # 왼쪽으로 90도 회전
                
            # 방향 갱신
            elif ele[1]=='D':
                current_dir= (current_dir+1)%4

            k,l = directions[current_dir]


print(cnt)#*******************************************
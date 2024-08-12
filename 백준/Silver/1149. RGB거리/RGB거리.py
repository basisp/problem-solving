import sys

N=int(input())
L=[]
for _ in range(N):
    L.append(list(map(int,sys.stdin.readline().split())))

dp=[[0]*3 for _ in range(N)]
dp[0]=L[0]

for i in range(1,N):
    for j in range(3):
        if j==0:
            dp[i][j]=min(dp[i-1][1],dp[i-1][2]) + L[i][j]
        elif j==1:
            dp[i][j]=min(dp[i-1][0],dp[i-1][2]) + L[i][j]
        elif j==2:
            dp[i][j]=min(dp[i-1][1],dp[i-1][0]) + L[i][j]


print(min(dp[N-1]))

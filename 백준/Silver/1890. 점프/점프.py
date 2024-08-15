import sys

n=int(input())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp=[[0]*(n+1) for _ in range(n+1)]
dp[1][1]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if dp[i][j]!=0 and arr[i-1][j-1]!=0:
            if i+arr[i-1][j-1]<=n:
                dp[i+arr[i-1][j-1]][j]+=dp[i][j]
            if j+arr[i-1][j-1]<=n:
                dp[i][j+arr[i-1][j-1]]+=dp[i][j]

print(dp[n][n])


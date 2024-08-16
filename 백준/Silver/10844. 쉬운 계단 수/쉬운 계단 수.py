import sys

n=int(input())

dp=[[0]*12 for _ in range(n+1)]

dp[1]=[0,0,1,1,1,1,1,1,1,1,1,0]

if n>=2:
    for i in range(2,n+1):
        for j in range(1,11):
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n])%1000000000)
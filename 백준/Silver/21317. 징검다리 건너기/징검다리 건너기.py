import sys

n=int(input())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n-1)]

k=int(input())

dp=[[float('inf')]*2 for _ in range(n+1)]

dp[1][0]=dp[1][1]=0

for i in range(1,n):
    #작점
    dp[i+1][0]=min(dp[i+1][0],dp[i][0]+arr[i-1][0])
    dp[i+1][1]=min(dp[i+1][1],dp[i][1]+arr[i-1][0])
    #큰점
    if i+2<=n:
        dp[i+2][0]=min(dp[i+2][0],dp[i][0]+arr[i-1][1])
        dp[i+2][1]=min(dp[i+2][1],dp[i][1]+arr[i-1][1])
    #엄큰점
    if i+3<=n:
        dp[i+3][1]=min(dp[i+3][1],dp[i][0]+k)


print(min(dp[n]))
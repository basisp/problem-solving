import sys

input=sys.stdin.readline

n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]

dp=[0]*(n+1)


for i in range(n-1,-1,-1):
    a,b=arr[i]
    
    if i+a<=n:
        dp[i]=max(dp[i+a]+b,dp[i+1])
    else:
        dp[i]=dp[i+1]
    
print(max(dp))
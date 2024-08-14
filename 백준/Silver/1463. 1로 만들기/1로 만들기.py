import sys
import math
n=int(input())

dp=[0]*(n+1)


if n>=2:
    dp[2]=1
    for i in range(2,n+1):
        min_v=math.inf
        min_v=min(min_v,dp[i-1]+1)
        if i%3==0:
            min_v=min(min_v,dp[i//3]+1)
        if i%2==0:
            min_v=min(min_v,dp[i//2]+1)
        
        dp[i]=min_v


print(dp[n])
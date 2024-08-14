import sys
import math
n=int(input())

dp=[0]*50001
dp[1]=1
for i in range(2,n+1):
    minimum=math.inf
    for k in range(1, int(math.sqrt(i))+1):
        minimum=min(minimum, dp[i-k**2])
    dp[i]=minimum+1

print(dp[n])
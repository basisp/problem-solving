import sys

C,N=map(int,sys.stdin.readline().split())


arr=[]
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

import math
dp=[math.inf]*(C+100)
dp[0]=0
for cost, num_people in arr:
    for i in range(num_people,C+100):
        dp[i]=min(dp[i],dp[i-num_people]+cost)

print(min(dp[C:]))

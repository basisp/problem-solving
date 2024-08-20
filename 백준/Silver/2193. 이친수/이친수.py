import sys


n=int(input())

#이친수는 0으로 시작하지 않는다.
#이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

dp=[0]*(n+1)
dp[1]=1
    
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])

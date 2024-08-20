import sys

n=int(input())

arr=[1,2,5,7]

dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=i

#사용할 수 있는 동전의 최소 개수

for ele in arr:
    if ele<=n:
        dp[ele]=1
    for i in range(1,n+1):
        if i-ele>=0:
            dp[i]=min(dp[i],dp[i-ele]+dp[ele])
print(dp[n])


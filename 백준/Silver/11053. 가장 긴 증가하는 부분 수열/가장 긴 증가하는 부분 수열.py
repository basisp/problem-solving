import sys
n=int(input())

arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(n+1)
dp[1]=1


for i in range(1,n+1):
    mx=0
    for j in range(0,i):
        if arr[i-1]>arr[j-1]:
            mx=max(mx,dp[j])
    dp[i]=mx+1

print(max(dp))
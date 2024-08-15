import sys

n=int(input())
arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*1001


for i in range(1,n+1):
    mx=0
    for j in range(0,i-1):
        if arr[j]<arr[i-1]:
            mx=max(mx,dp[j+1])
    dp[i]=mx+arr[i-1]

print(max(dp))

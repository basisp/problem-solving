import sys

n,k=map(int, sys.stdin.readline().split())

arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(n+1)
dp[1]=1
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if (j-i)*(1+abs(arr[i-1]-arr[j-1]))<=k and dp[i]!=0:
            dp[j]+=dp[i]

if dp[n]:
    print('YES')
else:
    print('NO')


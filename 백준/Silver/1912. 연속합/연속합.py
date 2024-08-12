import sys

n=int(input())

dp=[0]*n
L=list(map(int,sys.stdin.readline().split()))

dp[0]=L[0]

if max(L)<0:
    ans=max(L)

else:
    for i in range(1,n):
        dp[i]=max(0, dp[i-1]+L[i])
    ans=max(dp)

print(ans)


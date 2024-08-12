import sys

n=int(input())

dp=[0]*n
L=list(map(int,sys.stdin.readline().split()))

dp[0]=L[0]

for i in range(1,n):
    dp[i]=max(L[i],dp[i-1]+L[i])



print(max(dp))
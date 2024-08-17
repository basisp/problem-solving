#최소비용 , 항상 순서대로 곱샘 가능


import sys

n=int(input())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dp=[[0]*(n+1) for _ in range(n+1)]

for k in range(1,n+1):
    for i in range(1,n-k+1):
        j=i+k
        dp[i][j]=min(dp[i][t]+dp[t+1][j]+(arr[i-1][0]*arr[t-1][1]*arr[j-1][1]) for t in range(i,j)) 


print(dp[1][n])
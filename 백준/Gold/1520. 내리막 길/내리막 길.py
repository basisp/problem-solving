#항상 높이가 더 낮은 지점으로만 이동하여
#계속 감소하는 행렬

import sys

m,n=map(int,sys.stdin.readline().split())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(m)]

dp=[[-1]*(n+1) for _ in range(m+1)]

dp[m][n]=1

def dfs(i,j):
    if dp[i][j]!=-1:
        return dp[i][j]
    
    sum=0
    if i<=m-1 and arr[i-1][j-1]>arr[i][j-1]:
        sum+=dfs(i+1,j)
    if j<=n-1 and arr[i-1][j-1]>arr[i-1][j]:
        sum+=dfs(i,j+1)
    if i-2>=0 and arr[i-1][j-1]>arr[i-2][j-1]:
        sum+=dfs(i-1,j)   
    if j-2>=0 and arr[i-1][j-1]>arr[i-1][j-2]:
        sum+=dfs(i,j-1)   
    dp[i][j]=sum

    return dp[i][j]


print(dfs(1,1))

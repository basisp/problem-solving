import sys
n=int(input())

arr=[int(input()) for _ in range(n)]

dp=[[0]*3 for _ in range(n+1)]

dp[1]=[0,arr[0],arr[0]]

for i in range(2,n+1):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    dp[i][1]=dp[i-1][0]+arr[i-1]
    dp[i][2]=dp[i-1][1]+arr[i-1]

ans=0
for ele in dp:
    mx=max(ele)
    ans=max(ans,mx)

print(ans)
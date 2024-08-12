import sys

n=int(input())

L=[]
for _ in range(n):
    L.append(list(map(int,sys.stdin.readline().split())))

dp=[[0]*n for _ in range(n)]

dp[0][0]=L[0][0]

if n==1:
    print(L[0][0])
else:    
    for i in range(n):
        for j in range(len(L[i])):
            if j==0:
                dp[i][j]=L[i][j]+dp[i-1][j]
            elif j==len(L[i])-1:
                dp[i][j]=L[i][j]+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+L[i][j]

    print(max(dp[n-1]))
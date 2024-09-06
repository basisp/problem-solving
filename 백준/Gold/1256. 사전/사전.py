import sys

n,m,k=map(int,sys.stdin.readline().split())

dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,m+1):
    dp[0][i]=1
for i in range(1,n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]

if dp[n][m]<k:
    print(-1)
else:
    ans=[]

    i=n
    j=m

    while True:
        if k<=dp[i-1][j]:
            ans.append('a')
            i-=1
        else:
            k-=dp[i-1][j]
            ans.append('z')
            j-=1

        if i==0:
            for _ in range(j):
                ans.append('z')
            break
        if j==0:
            for _ in range(i):
                ans.append('a')
            break

    print(''.join(ans))
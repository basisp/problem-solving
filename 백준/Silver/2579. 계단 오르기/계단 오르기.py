import sys

#1 or 2 계단을 오를 수 있음 
#연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
#마지막은 무조건 밟음

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

dp=[[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(3):
        if j==0:
            dp[i][j]=max(dp[i-1][1],dp[i-1][2])
        elif j==1:
            dp[i][j]=dp[i-1][0]+arr[i-1]
        elif j==2:
            dp[i][j]=dp[i-1][1]+arr[i-1]


print(max(dp[n][1],dp[n][2]))
import sys

T=int(input())

def main():
    for _ in range(T):
        n=int(input())
        L=[]
        for _ in range(2):
            L.append(list(map(int,sys.stdin.readline().split())))
        solve(n,L)

def solve(n,L):
    dp=[[0]*(n+1) for _ in range(2)]
    dp[0][1]=L[0][0]
    dp[1][1]=L[1][0]

    for i in range(2,n+1):
        dp[0][i]=max(dp[1][i-1]+L[0][i-1], dp[1][i-2]+L[0][i-1])
        dp[1][i]=max(dp[0][i-1]+L[1][i-1], dp[0][i-2]+L[1][i-1])

    print(max(dp[0][n],dp[1][n]))

main()
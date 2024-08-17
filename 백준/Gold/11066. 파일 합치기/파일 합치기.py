import sys
input=sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))

        solve(n, arr)

def solve(n, arr):
    dp = [[0]*n for _ in range(n)]

    for k in range(2, n+1):  
        for i in range(n-k+1):
            j = i+k-1
            dp[i][j]=min(dp[i][t] + dp[t+1][j] for t in range(i,j))+sum(arr[i:j+1])

    print(dp[0][n - 1])


main()

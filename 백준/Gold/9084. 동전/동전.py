import sys
input=sys.stdin.readline

T=int(input())

def solve(n,arr,m):
    dp=[0]*(m+1)
    dp[0]=1
    for ele in arr:
        for i in range(1,m+1):
            if i-ele>=0:
                dp[i]+=dp[i-ele]
    print(dp[m])


for _ in range(T):
    n=int(input())
    arr=list(map(int,input().split()))
    m=int(input())
    solve(n,arr,m)
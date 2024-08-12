import sys 

T=int(input())

dp= [0]*101
dp[1]=dp[2]=dp[3]=1
dp[4]=dp[5]=2

def f(N):
    
    if dp[N]:
        return dp[N]
    else:
        dp[N]=f(N-1)+f(N-5)
        return dp[N]

for _ in range(T):
    print(f(int(input())))

import sys
input= sys.stdin.readline

n=int(input())
weights=list(map(int,input().split()))

m=int(input())
target=list(map(int,input().split()))

dp=[[0]*15001 for _ in range(31)]

def cal(num,weight):
    if num>n: return

    if dp[num][weight]: return

    dp[num][weight]=1
    
    if num<n:
        cal(num+1, weight+weights[num-1])
        cal(num+1, abs(weight- weights[num-1]))
    cal(num+1, weight)

cal(0,0)

for t in target:
    if t>15000: print("N",end=' ')
    elif dp[n][t]: print('Y',end=' ')
    else: print('N',end=' ')
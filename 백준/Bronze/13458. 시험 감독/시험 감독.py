import sys
import math
input=sys.stdin.readline
n=int(input())

arr=list(map(int, input().split()))

B,C=list(map(int, input().split()))


#B는 1번만 C는 여러번
#감독 쓰는 경우 안쓰는 경우 나눠서 최소 구하면 될듯
arr_B=[]
for ele in arr:
    arr_B.append(ele-B)
dp=[0]*(n+1)
for i in range(1,n+1):
    if arr_B[i-1]<=0:
        dp[i]=1
    else:
        dp[i]=math.ceil(arr_B[i-1]/C)+1
print(sum(dp))
    


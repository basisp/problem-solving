import sys

input = sys.stdin.readline

N=int(input())

A=[0]+list(map(int,input().split()))+[0]
#dp -> 인덱스까지의 최장 길이, 인덱스 -> arr의 인덱스
dp=[0]*(N+2)

#바텀 업
for i in range(1,N+1):
    for j in range(0,i):
        if A[j]<A[i]:
            dp[i]=max(dp[j]+1,dp[i])

#A.reverse()로 할 경우 dp2 도 계산 후 reverse 해줘야 함. dp2는 dp랑 맞물려서 저장해야
dp2=[0]*(N+2)
for i in range(N,0,-1):
    for j in range(N+1,i,-1):
        if A[j]<A[i]:
            dp2[i]=max(dp2[j]+1,dp2[i])

max_bitonic=0 
for i in range(1,N+1):
    max_bitonic = max(max_bitonic, dp[i]+dp2[i])

#i에 해당되는 게 중복으로 계산되니까
print(max_bitonic-1)
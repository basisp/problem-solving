import sys

n=int(input())

arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#같은 수 연속 개수 최대

dp=[[0]*(n+1) for _ in range(6)]


t=[1,2,3,4,5]

for ele in t:
    for i in range(n):
        if ele in arr[i]:
            dp[ele][i+1]=dp[ele][i]+1

max_v=0
min_v=6
for i in range(1,6):
    for ele in dp[i]:
        max_v=max(max_v,ele)
for i in range(1,6):
    if max_v in dp[i]:
        min_v=i
        break
print(max_v,min_v,sep=' ')

 
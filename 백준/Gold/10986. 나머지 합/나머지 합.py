import sys

N,M=map(int, input().split())

S=list(map(int, sys.stdin.readline().split()))


prefix_sum=[0]*N
prefix_sum[0]=S[0]
for i in range(1,N):
    prefix_sum[i]=prefix_sum[i-1]+S[i]

remainder_count=[0]*M

for i in range(N):
    remainder=prefix_sum[i]%M
    remainder_count[remainder]+=1


count=remainder_count[0]
for r in remainder_count:
    count+=(r*(r-1))//2

print(count)
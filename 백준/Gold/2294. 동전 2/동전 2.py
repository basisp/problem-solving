# 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.
#가치가 같은 동전이 여러 번 주어질 수도 있다.

n,k = map(int,input().split())
arr=set()
for _ in range(n):
    num=int(input())
    arr.add(num)
n=len(arr)
mx=max(arr)
dp=[1e7]*(100001)
for ele in arr:
    if ele<=k:
        dp[ele]=1

for ele in arr:
    for i in range(ele,k+1):
        if i-ele>=0:
            dp[i]=min(dp[i],dp[i-ele]+dp[ele])

if dp[k]>=1e7:
    print(-1)
else:
    print(dp[k])


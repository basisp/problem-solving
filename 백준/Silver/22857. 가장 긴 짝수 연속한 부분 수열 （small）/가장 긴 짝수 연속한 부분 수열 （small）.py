import sys
input=sys.stdin.readline

n,k = map(int,input().split())
arr=list(map(int,input().split()))

dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(k+1):
        if arr[i-1]%2==0: #짝수면 전체증가
            dp[i][j]=dp[i-1][j]+1
        elif j!=0 and arr[i-1]%2==1: #홀수면 무조건 삭제 -> k=0 이면  arr[i-1]부터 새배열 시작 따라서 0(초기화 값 그대로), 나머지는 삭제했으니까 k는 1 증가, 따라서 지금 k 보다 하나 작은 dp[i-1][j-1]에서 불러오기
            dp[i][j]=dp[i-1][j-1]

max_v=0
for ele in dp:
    tmp=max(ele)
    max_v=max(max_v,tmp)
print(max_v)
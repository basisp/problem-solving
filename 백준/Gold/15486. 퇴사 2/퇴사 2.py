import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (N + 1)

for i in range(N):
    A, B = arr[i]

    if i + 1 <= N:
        dp[i + 1] = max(dp[i + 1], dp[i])

    if i + A <= N:
        dp[i + A] = max(dp[i + A], dp[i] + B)

print(dp[N])

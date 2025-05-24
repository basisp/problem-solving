

T = int(input())
for test_case in range(1, T + 1):

    N, L = map(int, input().split())  # 재료 수, 제한 칼로리
    ingredients = [list(map(int, input().split())) for _ in range(N)]  # 점수, 칼로리

    dp = [0] * (L + 1)  # dp[i]: i칼로리 이하로 만들 수 있는 최대 점수

    for score, cal in ingredients:
        for j in range(L, cal - 1, -1):  # 뒤에서부터 순회 (중복 방지)
            dp[j] = max(dp[j], dp[j - cal] + score)
    print(f"#{test_case} {max(dp)}")

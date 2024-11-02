import bisect
from itertools import combinations

N, C = map(int, input().split())
weight = list(map(int, input().split()))

# 배열을 반으로 나눔
mid = N // 2
left_weight = weight[:mid]
right_weight = weight[mid:]

# 부분집합의 합을 구하는 함수
def get_subset_sums(arr):
   sums = []
   n = len(arr)
   for i in range(n+1):  # 0개부터 n개까지 선택
       for combo in combinations(arr, i):
           total = sum(combo)
           if total <= C:
               sums.append(total)
   return sorted(sums)

# 각 부분의 부분집합의 합을 구함
left_sums = get_subset_sums(left_weight)
right_sums = get_subset_sums(right_weight)

# 개수 세기
answer = 0
for left in left_sums:
    remain = C - left
    answer += bisect.bisect_right(right_sums, remain)

print(answer)
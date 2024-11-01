import sys

n, s = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
total = 0
final_length = float('inf')  # 최소 길이를 저장할 변수 초기화

while end < n:  # end는 n보다 작아야 함
    total += arr[end]  # 현재 end의 값을 total에 더함
    end += 1  # end 포인터 증가

    while total >= s:  # total이 s 이상이면
        final_length = min(final_length, end - start)  # 길이 업데이트
        total -= arr[start]  # start의 값을 total에서 빼기
        start += 1  # start 포인터 증가

if final_length == float('inf'):  # 유효한 부분 수열을 찾지 못한 경우
    print(0)
else:
    print(final_length)

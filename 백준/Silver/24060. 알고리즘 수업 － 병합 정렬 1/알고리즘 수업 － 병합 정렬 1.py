import sys

sys.setrecursionlimit(100000)
#병합정렬
N, K=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
cnt=0
C=0
def merge_sort(A,p,r):  # A[p..r]을 오름차순 정렬한다.
    global C
    if (p < r) and C==0:
        q= (p + r) // 2       # q는 p, r의 중간 지점
        merge_sort(A, p, q)    # 전반부 정  렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)    # 병합
    
# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    global cnt, C
    i = p
    j = q + 1
    tmp = []
    
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        i += 1

    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        j += 1

    for i in range(len(tmp)):
        A[p + i] = tmp[i]
        cnt += 1
        if cnt == K:
            print(A[p + i])
            C = 1
            return



merge_sort(A,0,N-1)

if cnt<K:
    print(-1) 
import sys

K, N = map(int, sys.stdin.readline().split())
L = []

for _ in range(K):
    L.append(int(sys.stdin.readline().strip()))


start = 1
end = max(L)  

def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        count = sum(x // mid for x in L)
        
        if count >= N:
            result = mid  
            start = mid + 1 
        else:
            end = mid - 1  
    
    return result


print(binary_search(start, end))

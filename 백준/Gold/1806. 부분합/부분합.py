import sys

n,s = map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))

start = 0
end = 0
total=arr[start]
final_length = n+1

while end < n:

    if total>=s:
        final_length=min(final_length, end-start+1)
        total-=arr[start]
        start+=1
    else:
        end+=1
        if end==n:
            break
        total+=arr[end]


if final_length<n+1:
    print(final_length)
else:
    print(0)
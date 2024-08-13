import sys

input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
t=len(arr)
length=[1]*t

for k in range(t):
    for i in range(k):
        if arr[i][1]<arr[k][1]:
            length[k]=max(length[k],length[i]+1)


print(n-max(length))

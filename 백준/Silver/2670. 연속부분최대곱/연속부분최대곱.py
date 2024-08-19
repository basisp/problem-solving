import sys

n=int(input())

arr=[]
for _ in range(n):
    arr.append(float(input()))

sum=arr[0]
max_v=arr[0]

for i in range(1,n):
    sum=max(arr[i],sum*arr[i])

    max_v=max(max_v,sum)

print(f'{max_v:.3f}')

import sys


n=int(input())
if n==1:
    print(0)
    exit()
    
a = [False,False] + [True]*(n-1)
lis=[]

for i in range(2,n+1):
  if a[i]:
    lis.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

cnt=0
t=len(lis)
start=0
end=0
total=lis[0]
while end<t:
    if total<n:
        end+=1
        if end==t:
            break
        total+=lis[end]
    elif total == n:
        cnt+=1
        total-=lis[start]
        start+=1
        end+=1
        if end==t:
            break
        total+=lis[end]
    else:
        total-=lis[start]
        start+=1


print(cnt)
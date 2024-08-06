import sys
N=int(input())

L=[]
for _ in range(N):
    x,y=map(int,input().split())    
    L.append([x,y])

L.sort(key=lambda x: (x[1],x[0]))

cnt=1
tmp=0

for i in range(N-1):
    if L[tmp][1]<=L[i+1][0]:
        cnt+=1
        tmp=i+1

print(cnt)

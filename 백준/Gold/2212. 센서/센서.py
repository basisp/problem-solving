import sys 

N=int(input())

K=int(input())

L=list(map(int,sys.stdin.readline().split()))

L.sort()

dif=[]

for i in range(1,N):
    dif.append(L[i]-L[i-1])

dif.sort()

for _ in range(K-1):
    if dif:
        dif.pop()

print(sum(dif))


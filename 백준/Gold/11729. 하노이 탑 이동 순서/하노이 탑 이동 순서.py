import sys

N=int(input())
L=[]
cnt=0
def hanoi(start,mid,end,N):
    if N==1:
        L.append([start,end])
        return 1
    else:
        return hanoi(start,end,mid,N-1)+hanoi(start,mid,end,1)+hanoi(mid,start,end,N-1)

print(hanoi(1,2,3,N))

for A,B in L:
    print(A,B,sep=' ')

import sys
import math
K=int(input())

a=0
while 2**a<K:
    a+=1
A=2**a

cnt=0
dif=A
if A!=K:
    while K:
        if K-dif//2>=0:
            K=K-dif//2
            dif//=2
            cnt+=1
        else:
            dif//=2
            cnt+=1
    print(A,cnt,sep=' ')
    
else:
    print(A,0,sep=' ')

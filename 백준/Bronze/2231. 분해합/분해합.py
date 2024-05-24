import sys
from collections import deque

val=int(input())
res=[]

def calculate(val):
    for x in range(1,10000001):
        sum=0
        str_num=str(x)
        for element in str_num:
            sum+=int(element)
        sum+=x

        if sum==val:
            res.append(x)
                
    if len(res)==0:
        return 0
    else:
        return min(res)
    
    
print(calculate(val))
        
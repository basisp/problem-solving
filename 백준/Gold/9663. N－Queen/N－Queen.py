import sys
from collections import deque

n=int(input())

graph=[[0]*n for _ in range(n)]

ans=0

v1=[0]*n #행
v2=[0]*(2*n-1)# 증가하는 위 대각
v3=[0]*(2*n-1)# 감소하는 아래 대각

def dfs(num): #cnt는 행번호
    global ans
    if num==n:
        ans+=1
        return
    
    for i in range(n):
        if v1[i]!=1 and v2[num+i]!=1 and v3[num-i]!=1:
            v1[i]=1
            v2[num+i]=1
            v3[num-i]=1
            dfs(num+1)
            v1[i]=0
            v2[num+i]=0
            v3[num-i]=0

dfs(0)
print(ans)
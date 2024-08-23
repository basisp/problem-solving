import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    A,B=map(int,input().split())
    res=[]
    visited=[0]*10000
    visited[A]=1
    Q=deque([[A,'']])

    while Q:
        num,cmd=Q.popleft()
        if num==B:
            print(cmd)
            break        

        tmp=(num*2)%10000
        if visited[tmp]==0:
            visited[tmp]=1
            Q.append([tmp,cmd+'D'])

        tmp=num-1
        if tmp==-1:
            tmp=9999
        if visited[tmp]==0:
            visited[tmp]=1
            Q.append([tmp,cmd+'S'])
               
        #L
        tmp= ((num%1000)*10)+(num//1000)
        if visited[tmp]==0:
            visited[tmp]=1
            Q.append([tmp,cmd+'L'])

        tmp=(num%10)*1000+(num//10)
        if visited[tmp]==0:
            visited[tmp]=1
            Q.append([tmp,cmd+'R'])        



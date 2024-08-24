# 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 
# 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다.
#연결되는 경우 + 위아래가 같은경우
import sys
input=sys.stdin.readline
n=int(input())

graph=[0]*(n+1)
res=[]
for i in range(1,n+1):
    graph[i]=int(input())

def dfs(i):
    global ans
    if visited[i]==0:
        visited[i]=1    
        top.add(i)
        bottom.add(graph[i])
    
        if top==bottom:
            ans=1
            return

        dfs(graph[i])
    return

res=set()
for i in range(1,n+1):
    ans=0
    top=set()
    bottom=set()
    visited=[0]*(n+1)
    dfs(i)
    if ans==1:
        for ele in top:
            res.add(ele)
res=sorted(res)
print(len(res))
for ele in res:
    print(ele)
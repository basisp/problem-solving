import sys
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)  

def back(k,num,visited): #k는 현재 횟수 , num은 시작 숫자, visited는 방문표
    global res
    if k==5:
        res=1
        return
    
    for ele in graph[num]:
        if visited[ele]==0:
            visited[ele]=1
            back(k+1,ele,visited)
            visited[ele]=0
    

res=0  
for i in range(n):
    visited=[0]*n
    visited[i]=1
    back(1,i,visited)
    if res==1:
        print(res)
        quit()
print(0)
                
    
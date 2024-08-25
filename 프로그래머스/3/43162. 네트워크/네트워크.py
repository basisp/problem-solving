import sys
sys.setrecursionlimit(10**5)

visited=[0]*(201)

def solution(n, computers):
    
    cnt=0
    for i in range(n):
        if visited[i]==0:
            dfs(i,computers)
            cnt+=1
    return cnt
    
    
def dfs(v,computers):
    visited[v]=1
    

    for j in range(len(computers)):
        if j!=v and computers[v][j]==1 and visited[j]==0 :
            dfs(j,computers)
    
    

            
        
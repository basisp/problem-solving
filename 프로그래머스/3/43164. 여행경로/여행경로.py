ans=[]

def dfs(res,visited,tickets):
    global ans
    if len(res)==len(tickets)+1:
        ans.append(res[:])
        return
    
    for i in range(len(tickets)):
        if visited[i]==0 and tickets[i][0]==res[-1]:
            visited[i]=1
            res.append(tickets[i][1])
            dfs(res,visited,tickets)
            visited[i]=0
            res.pop()
            

def solution(tickets):
    global ans
    visited=[0]*len(tickets)
    res=['ICN']
    dfs(res,visited,tickets)
    
    
    
    ans.sort()
    return ans[0]

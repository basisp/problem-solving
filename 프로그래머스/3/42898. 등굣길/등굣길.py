
def bfs(graph,a,b,n,m):
    if a==n and b==m:
        return 1
    
    if graph[a][b]!=0:
        return graph[a][b]
    
    for dn,dm in [(0,1),(1,0)]:
        na=dn+a ; nb=dm+b
        if 1<=na<=n and 1<=nb<=m and graph[na][nb]!=-1:
            graph[a][b]+=bfs(graph,na,nb,n,m)
    
    return graph[a][b]
            
def solution(m, n, puddles):
    
    graph=[[0]*(m+1) for _ in range(n+1)]
    for b,a in puddles:
        graph[a][b]=-1
    
    return bfs(graph,1,1,n,m)%1000000007
    
        
    
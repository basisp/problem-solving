def solution(triangle):
    dp=[[0]*len(t) for t in triangle]
    dp[0][0]=triangle[0][0]
    
    for i in range(len(dp)-1):
        for j in range(len(dp[i])):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j]+triangle[i+1][j])
            dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+triangle[i+1][j+1])
            
    return max(dp[-1])
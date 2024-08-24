def solution(arr):  
    min_dp=[[11000000]*(len(arr)) for _ in range(len(arr))]
    max_dp=[[-11000000]*(len(arr)) for _ in range(len(arr))]
    
    
    for i in range(0,len(arr),2):
        min_dp[i][i]=int(arr[i])
        max_dp[i][i]=int(arr[i])
    
    n=len(arr)
    #size 먼저
    for size in range(2,n,2): #홀수로 증가
        for i in range(0,n-size,2):
            j=i+size
            for k in range(i+1,j,2):  #k는 연산자의 위치 = 홀수
                if arr[k]=='+':
                    min_dp[i][j]=min(min_dp[i][j],min_dp[i][k-1]+min_dp[k+1][j])
                    max_dp[i][j]=max(max_dp[i][j],max_dp[i][k-1]+max_dp[k+1][j])
                else:
                    min_dp[i][j]=min(min_dp[i][j],min_dp[i][k-1]-max_dp[k+1][j])        
                    max_dp[i][j]=max(max_dp[i][j],max_dp[i][k-1]-min_dp[k+1][j])
    
                
    return max_dp[0][n-1]
                    

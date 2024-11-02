def solution(money):
    n=len(money)
    dp1=[0]*n
    dp2=[0]*n
    
    #첫 집을 무조건 터는 경우
    dp1[0]=money[0]
    dp1[1]=money[0]
    
    for i in range(2,n-1):
        dp1[i]=max(dp1[i-1],dp1[i-2]+money[i])    

    #첫 집을 안터는 경우
    dp2[1]=money[1]
    
    for i in range(2,n):
        dp2[i]=max(dp2[i-1],dp2[i-2]+money[i])
        
    return max(dp1[n-2],dp2[n-1])
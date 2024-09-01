res=[]

def dfs(n, num,numbers ):
    
    if n==len(numbers):
        res.append(num)
        return
    
    dfs(n+1,num+numbers[n],numbers)
    dfs(n+1,num-numbers[n],numbers)
    
    
    
def solution(numbers,target):
    dfs(0,0,numbers)
    cnt=0
    for ele in res:
        if ele==target:
            cnt+=1
    return cnt
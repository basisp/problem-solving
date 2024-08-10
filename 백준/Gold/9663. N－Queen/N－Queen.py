import sys

N=int(input())

#한 열 
column=[0]*100
#대각선
cross1=[0]*100
cross2=[0]*100

res=0

def back(cnt:int):
    global res
    if cnt==N:
        res+=1
        return
    
    for i in range(N):
        if column[i] or cross1[i+cnt] or cross2[cnt-i+N-1]:
            continue
        column[i]=1
        cross1[i+cnt]=1
        cross2[cnt-i+N-1]=1
        back(cnt+1)
        column[i]=0
        cross1[i+cnt]=0
        cross2[cnt-i+N-1]=0


back(0)
print(res)

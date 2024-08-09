import sys

N,C=map(int, sys.stdin.readline().split())
L=[]
for _ in range(N):
    L.append(int(input()))
L.sort()

def binary():
    start=1
    end=L[-1]-L[0]

    while start<=end:
        mid=(start+end)//2
        #여기서 집의 위치 -> 차로 어떻게 연결하지
        if home_check(mid):
            result=mid
            start=mid+1
        else:
            end=mid-1
    
    return result

#그리디
def home_check(mid):
    count=1 #일단 어딘지는 모르겠는데 집을 설치해
    last_installed_house=L[0]

    for i in range(1,N):
        if L[i]-last_installed_house>=mid:
            count+=1
            last_installed_house=L[i]
            
        if count>=C:
            return True
    
    return False


print(binary())
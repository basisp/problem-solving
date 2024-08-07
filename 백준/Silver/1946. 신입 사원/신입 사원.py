import sys

T=int(input())

L=[]

def main():
    for _ in range(T):
        N=int(input())
        for _ in range(N):
            L.append(list(map(int,sys.stdin.readline().split())))
        L.sort()
        func(L,N)
        L.clear()

def func(L,N): #메모리를 잡아먹음
    cnt=0
    min=L[0][1]

    for i in range(1, N):
        if L[i][1]>min:
            cnt+=1
        if min>L[i][1]:
            min=L[i][1]
        


    print(N-cnt)

main()



import sys

N=int(input()) #범위가 천만까지
#주어지는 수는 10000까지

C=[0]*100001

for _ in range(N):
    x=int(sys.stdin.readline())
    C[x]+=1

C_stack=C.copy()

for i in range(1,10001):
    C_stack[i]=C_stack[i-1]+C_stack[i]

for i in range(0,10001):
    while C[i]!=0:
        print(i)
        C[i]-=1

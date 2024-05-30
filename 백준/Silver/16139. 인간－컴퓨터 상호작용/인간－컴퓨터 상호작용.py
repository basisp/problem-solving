import sys

S=list(sys.stdin.readline().rstrip())
q=int(input()) #200000

T=[[0]*26 for _ in range(len(S))]


for i in range(len(S)):
    T[i][ord(S[i])-97]+=1

for _ in range(q):
    K=sys.stdin.readline().split()
    x=ord(K[0])-97
    cnt=0
    for i in range(int(K[1]),int(K[2])+1):
        if T[i][x]==1:
            cnt+=1
    print(cnt)


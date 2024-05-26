import sys

N=int(input())

S=[]
S_1=[]
for _ in range(N):
    k=sys.stdin.readline().rstrip()
    if k not in S_1:
        S_1.append(k)
        S.append([len(k),k])

N=len(S)


S.sort()


for element in S:
    print(element[1])


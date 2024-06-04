import sys
import math


#M이상 N이하의 소수를 모두 출력

M,N= map(int, sys.stdin.readline().split())

if M==1:
    M+=1

S=[0]*(N+1)
for i in range(M,N+1):
    S[i]=i

for k in range(2, int(math.sqrt(N))+1):
    for i in range(k+k,N+1,k):
        S[i]=0

for element in S:
    if element !=0:
        print(element)

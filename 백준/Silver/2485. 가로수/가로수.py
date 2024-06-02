import sys
import math
N=int(input())
S=[]
for _ in range(N):
    S.append(int(input()))

S_minus=[0]*(N-1)
for i in range(N-1):
    S_minus[i]=S[i+1]-S[i]

x=S_minus[0]
for element in S_minus:
    x=math.gcd(x,element)

#S[0]+x*?=S[N-1]
y=(S[N-1]-S[0])//x+1

print(y-N)

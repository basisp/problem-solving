import sys

A,B=map(int,sys.stdin.readline().split())
C,D=map(int,sys.stdin.readline().split())

#B,D의 최소공배수 구하기

def gcd(B,D):
    if B<D:
        B,D=D,B
    while D:
        B,D=D,B%D
    return B

def lcm(B,D):
    return B*D//gcd(B,D)

x=lcm(B,D)
A=(x//B)*A
C=(x//D)*C

k=A+C
j=x

y=gcd(k,j)

print(k//y,j//y,sep=' ')
import sys

A,B=map(int,sys.stdin.readline().split())


def gcd(A,B): #참조로 전달?
    if B>A:
        A,B= B,A
    while B:
        A,B=B,A%B
    return A

def lcm(A,B):
    return A*B//gcd(A,B)

print(lcm(A,B))
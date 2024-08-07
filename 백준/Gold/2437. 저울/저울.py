import sys 

N=int(input())

L=list(map(int,sys.stdin.readline().split()))

L.sort()


def func(L):
    total=0
    for i in range(len(L)):
        if total+1<L[i]:
            return total+1
        total+=L[i]
    return total+1

print(func(L))
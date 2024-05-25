import sys

N=int(input())

stack=[]
for _ in range(N):
    stack.append(int(input()))
stack.sort()
for element in stack:
    print(element)
import sys

N=int(input())

stack=list(map(int, sys.stdin.read().split()))

stack.sort()

for element in stack:
    print(element)
           
import sys


S=list(map(int, sys.stdin.read().split()))

for i in range(len(S)//2):
    print(S[2*i]+S[2*i+1])

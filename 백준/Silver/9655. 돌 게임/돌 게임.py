import sys

#1 or 3

n=int(input())

cnt=n%3

cnt+=n//3

if cnt%2==0:
    print("CY")
else:
    print("SK")


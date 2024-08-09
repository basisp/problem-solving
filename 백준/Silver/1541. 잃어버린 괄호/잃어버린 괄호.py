import sys

L=sys.stdin.readline().strip().split('-')
T=[]
for ele in L:
    tmp=ele.split('+')
    num=0
    for element in tmp:
        num+=int(element)
    T.append(num)

sum=T[0]

for i in range(1,len(T)):
    sum-=T[i]

print(sum)
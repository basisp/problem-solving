import sys
input=sys.stdin.readline
N=int(input())
Distance=list(map(int,input().split()))
Price=list(map(int,input().split()))
Price.pop()

total=0


needed_fuel=sum(Distance)

cnt=0
while True:
    if Price[cnt]==min(Price):
        total+=Price[cnt]*sum(Distance[cnt:])
        break
    else:
        total+=Price[cnt]*Distance[cnt]
        cnt+=1
        if cnt>N-1:
            break

print(total)


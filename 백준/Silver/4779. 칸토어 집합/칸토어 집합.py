import sys
sys.setrecursionlimit(10**5)

def func(start,end):
    if start==end:
        return
    
    n=end-start+1
    n//=3
    for i in range(start+n,end-n+1):
        L[i]=' '
    func(start,start+n-1)
    func(end-n+1,end)



T=list(map(int,sys.stdin.read().split()))
for num in T:
    N=num
    L=['-']*(3**N)
    func(0,len(L)-1)
    print(''.join(L))


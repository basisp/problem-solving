import sys
from collections import deque




class Heap:
    def __init__(self,*args):
        if len(args)!=0:
            self.A=args[0]
        else:
            self.A=[]


    def insert(self,x):
        self.A.append(x)
        self.perlocateUp(len(self.A)-1)

    def perlocateUp(self,i:int):
        parent=(i-1)//2
        if i>0 and self.A[i]>self.A[parent]: #i가 0이면 루트노드로 부모 노드가 존재하지 않음
            self.A[i], self.A[parent] =self.A[parent], self.A[i]
            self.perlocateUp(parent) #재귀적

    def deleteMax(self):
        if (not self.isEmpty()):
            max=self.A[0]
            if len(self.A) > 1:
                self.A[0]=self.A.pop()
                self.perlocateDown(0)
            else:
                self.A.pop()
            return max
        else:
            return None
        
    def perlocateDown(self,i:int):
        child=2*i+1 #left child
        right=2*i+2 #right child
        if(child<=len(self.A)-1): #인덱스이기 때문에 -1
            if(right<=len(self.A)-1 and self.A[child]<self.A[right]):
                child=right
            if self.A[i]<self.A[child]:
                self.A[i], self.A[child] = self.A[child], self.A[i]
                self.perlocateDown(child)

    def max(self):
        return self.A[0]
    
    def buildHeap(self):
        for i in range((len(self.A)-2)//2,-1,-1):
            self.perlocateDown(i) #맨끝 노드의 부모노드부터 시작

    def isEmpty(self)->bool:
        return len(self.A)==0
    
    def clear(self):
        self.A=[]

    def size(self):
        return len(self.A)
    


N=int(input())
A=Heap()

for i in range(N):
    val=int(sys.stdin.readline())

    if val==0:
        if A.isEmpty():
            print(0)
        else:
            print(A.deleteMax())


    else:
        A.insert(val)



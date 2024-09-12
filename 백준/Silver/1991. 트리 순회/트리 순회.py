import sys

n=int(input())
tree={}

for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root]=[left,right]

ans=[]
def precycle(node):
    left,right=tree[node]
    
    ans.append(node)
    if left!='.':
        precycle(left)
    
    if right!='.':
        precycle(right)
precycle('A')
print(''.join(ans))

def midcycle(node):
    left,right=tree[node]

    if left!='.':
        midcycle(left)
    
    ans.append(node)
    
    if right!='.':
        midcycle(right)
ans.clear()
midcycle('A')
print(''.join(ans))

def lastcycle(node):
    left,right=tree[node]

    if left!='.':
        lastcycle(left)

    if right!='.':
        lastcycle(right)

    ans.append(node)    

ans.clear()
lastcycle('A')
print(''.join(ans))

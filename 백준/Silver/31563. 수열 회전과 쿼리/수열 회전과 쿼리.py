import sys
from collections import deque

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)
    
    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]
    
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
    
    def query(self, l, r):
        l += self.n
        r += self.n + 1
        sum = 0
        while l < r:
            if l % 2 == 1:
                sum += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                sum += self.tree[r]
            l //= 2
            r //= 2
        return sum


N, Q = map(int, input().split())
S = list(map(int, sys.stdin.readline().split()))
segment_tree = SegmentTree(S)
rotation = 0

def get_actual_index(index, rotation, n):
    return (index - rotation + n) % n


for _ in range(Q):
    K = list(map(int, sys.stdin.readline().split()))
    
    if K[0] == 1:
        rotation += K[1]
    elif K[0] == 2:
        rotation -= K[1]
    elif K[0] == 3:
        l = get_actual_index(K[1] - 1, rotation, N)
        r = get_actual_index(K[2] - 1, rotation, N)
        
        if l <= r:
            print(segment_tree.query(l, r))
        else:
            print(segment_tree.query(l, N - 1) + segment_tree.query(0, r))

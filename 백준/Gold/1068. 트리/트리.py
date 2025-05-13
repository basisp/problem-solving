import sys
from collections import defaultdict

def main():
    N = int(input())
    parents = list(map(int, sys.stdin.readline().split()))
    # -1 은 루트노드

    delete_num = int(input())

    graph = defaultdict(list)

    for idx, ele in enumerate(parents):
        if ele != -1:
            graph[ele].append(idx)
        else:
            root = idx
    
    #leaf 
    res = 0
    
    if root != delete_num:
        stack = [root]
    else:
        print(0)
        return
    
    if N==2:
        print(1)
        return

    while stack:
        num = stack.pop()
        
        if graph[num]:
            values = graph[num]
        else:
            res+=1
            continue

        for ele in values:
            if ele != delete_num:
                stack.append(ele)
            else:
                if len(values) == 1 and num != root:
                    res+=1


    print(res)


if __name__ == "__main__":
    main()

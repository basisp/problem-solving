from collections import defaultdict

def solution(begin, target, words):
    
    graph=defaultdict(list)  
    words.insert(0,begin)
    for i in range(len(words)):
        for k in range(len(words)):
            cnt=0
            for t in range(len(words[i])):
                if words[i][t]!=words[k][t]:
                    cnt+=1
        
            if cnt==1:
                graph[words[i]].append(words[k])
    
    visited=defaultdict(bool)
    
    for ele in words:
        visited[ele]=0
        
    stack=[begin]
    answer = 1e7
    pre_answer=0
    while stack:
        t=stack.pop()
        if t==target:
            answer=min(answer,pre_answer)
        if visited[t]==0:
            visited[t]=pre_answer
        pre_answer+=1
        for ele in graph[t]:
            if visited[ele]==0:
                stack.append(ele)

    if answer==1e7:
        return 0
    else:
        return answer

        
def solution(participant, completion):
    dict = {}
    temp=0
    
    for ele in participant:
        dict[hash(ele)] = ele
        temp+=hash(ele)    
        
    for ele in completion:
        temp-=hash(ele)
        
    return dict[temp]
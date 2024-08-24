def solution(N, number):
    s=[set() for _ in range(9)]
    
    for i in range(1,9):
        s[i].add(int(str(N)*i))
        
    for i in range(2,9):
        for j in range(1,i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    s[i].add(op1+op2)
                    s[i].add(op1*op2)
                    s[i].add(op1-op2) ##? 음수여도 가능?
                    if op2!=0:
                        s[i].add(op1//op2)
        
    for i in range(1,9):
        if number in s[i]:
            return i
            
    return -1


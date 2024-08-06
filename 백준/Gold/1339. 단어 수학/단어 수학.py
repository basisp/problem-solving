import sys 

N=int(input())

Dic={}
for _ in range(N):
    word=input()
    word_len=len(word)
    for i in range(word_len):
        Dic[word[i]]= Dic.get(word[i],0) + 10**(word_len-i-1)


Dic=sorted(Dic.items(), key= lambda x:x[1], reverse=True)

total=0

for i in range(len(Dic)):
    total += Dic[i][1] * (9-i)


        
print(total)
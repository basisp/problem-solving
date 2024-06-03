import sys

S=sys.stdin.readline()

res=set()

#slicing s
for i in range(len(S)):
    for k in range(len(S)):
        if S[i:k]=='':
            continue
        else:
            res.add(S[i:k])

print(len(res))
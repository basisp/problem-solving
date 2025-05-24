def is_palindrom(str):
    if str == str[::-1]:
        return True
    else:
        return False

for order in range(1,11):
    offset = int(input())

    graph = [list(input().rstrip()) for _ in range(8)]
    res =0
    #가로
    for i in range(8):
        for j in range(0,8-offset+1):
            str = graph[i][j:j+offset]
            if is_palindrom(str):
                res+=1

    #세로
    for j in range(8):
        for i in range(0,8-offset+1):
            str = [graph[t][j] for t in range(i,i+offset)]
            if is_palindrom(str):
                res+=1

    print(f"#{order} {res}")




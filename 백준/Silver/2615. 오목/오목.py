import sys


graph = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

directions=[(0,1),(1,0),(1,1),(1,-1),(-1,1)]

for i in range(19):
    for j in range(19):
        if graph[i][j]!=0:
            curr=graph[i][j]
            for da,db in directions:
                na=i+da ; nb=j+db
                cnt=1
                while 0<=na<19 and 0<=nb<19 and graph[na][nb]==curr:
                    cnt+=1
                    na+=da; nb+=db
                na-=da;nb-=db
                if cnt==5:
                    if graph[i-da][j-db]!=curr:
                        print(curr)
                        if j<=nb:
                            print(i+1,j+1,sep=' ')
                        elif j>nb:
                            print(na+1,nb+1,sep=' ')

                        exit()

print(0)

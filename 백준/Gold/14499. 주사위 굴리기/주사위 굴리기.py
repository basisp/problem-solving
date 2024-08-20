import sys
input=sys.stdin.readline
n,m,x,y,k=map(int,input().split())

# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 
# 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 
# 칸에 쓰여 있는 수는 0이 된다
#주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다.

# 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

command=list(map(int,input().split()))

dice =[0]*7


def move(directions): #어차피 1칸씩만 이동이니까 수동으로 일일이 만들어줌
    if directions ==1:
        dice[1],dice[3],dice[4],dice[6]= dice[4],dice[1],dice[6],dice[3]
    elif directions ==2:
        dice[1],dice[3],dice[4],dice[6]=dice[3],dice[6],dice[1],dice[4]
    elif directions ==3:
        dice[1],dice[2],dice[5],dice[6]=dice[5],dice[1],dice[6],dice[2]
    elif directions ==4:
        dice[1],dice[2],dice[5],dice[6]=dice[2],dice[6],dice[1],dice[5]
    

dir=[[0,0],[0,1],[0,-1],[-1,0],[1,0]]

for cmd in command:
    if 0<=x+dir[cmd][0]<=n-1 and 0<=y+dir[cmd][1]<=m-1:
        x+=dir[cmd][0]
        y+=dir[cmd][1]

        move(cmd)
        if arr[x][y]==0:
            arr[x][y]=dice[6]
        else:
            dice[6]=arr[x][y]
            arr[x][y]=0

        print(dice[1])



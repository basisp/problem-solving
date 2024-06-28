import sys
sys.setrecursionlimit(10**5+1)
N,M,R = map(int, sys.stdin.readline().split())

E=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    E[a-1].append(b)
    E[b-1].append(a)

for l in range(N):
    E[l].sort()

visited=['NO' for _ in range(N)]
V=[i for i in range(N)]
order=[0 for _ in range(N)]
i=1
def dfs(V, E, R):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    global i
    if i<=N:
        if visited[R-1]=='NO':
            order[R-1]=i
            i+=1

        visited[R-1] = 'YES'  # 시작 정점 R을 방문 했다고 표시한다.
        for element in E[R-1]:  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)i
            if visited[element-1] == 'NO':
                dfs(V, E, element)

if __name__=='__main__':
    dfs(V, E, R)
    for k in range(N):
        print(order[k])

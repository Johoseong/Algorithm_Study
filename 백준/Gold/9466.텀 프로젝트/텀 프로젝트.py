import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x):
    global result
    visited[x] = 1
    team.append(x) #사이클을 이루는 팀을 확인하기 위함
    next_x = field[x]
    
    if visited[next_x]: #방문가능한 곳이 끝났는지
        if next_x in team: #사이클 가능 여부
            result += team[team.index(next_x):] #사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(next_x)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    field = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [0] * (n + 1)
    result = []

    for i in range(1, n + 1):
        if visited[i] == 0: #방문 안한 곳이라면
            team = []
            dfs(i) #DFS 함수 돌림
            
    print(n - len(result)) #팀에 없는 사람 수
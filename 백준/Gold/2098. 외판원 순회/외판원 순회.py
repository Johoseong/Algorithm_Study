import sys
input = sys.stdin.readline

def solve(i, route):
    if route == (1 << N - 1) - 1:
        if weight[i][0] != 0:
            return weight[i][0]
        else:
            return int(1e9)

    if dp[i][route] != 0:
        return dp[i][route]
    
    min_dist = int(1e9)
    for j in range(1, N):
        if weight[i][j] == 0: # i->j로 갈 수 없음
            continue
        if route & (1 << j - 1) != 0: # 이미 방문한 곳임
            continue

        min_dist = min(min_dist, solve(j, route | (1 << j - 1)) + weight[i][j])
    dp[i][route] = min_dist
    return min_dist

N = int(input())
dp = [[0] * (1 << N - 1) for _ in range(N)]
weight = [list(map(int, input().split())) for _ in range(N)]

print(solve(0, 0))
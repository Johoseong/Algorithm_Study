import sys
sys.setrecursionlimit(10 ** 8)

def dfs(r, c, h, dp):
    if dp[r][c] != -1:
        return dp[r][c]

    tmp = 0
    for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        next_r = r + d[0]
        next_c = c + d[1]

        if 0 <= next_r < M and 0 <= next_c < N and (field[next_r][next_c] < h):
            tmp += dfs(next_r, next_c, field[next_r][next_c], dp)
    dp[r][c] = tmp
    return dp[r][c]

M, N = map(int, sys.stdin.readline().split()) 
field = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
dp = [[-1] * (N) for _ in range(M)]
dp[M - 1][N - 1] = 1

print(dfs(0, 0, field[0][0], dp))
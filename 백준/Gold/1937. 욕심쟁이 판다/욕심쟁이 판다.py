import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]
    
    dp[r][c] = 1
    for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        n_r = r + d[0]
        n_c = c + d[1]

        if not (0 <= n_r < n and 0 <= n_c < n):
            continue
        if matrix[n_r][n_c] <= matrix[r][c]:
            continue
        dp[r][c] = max(dp[r][c], dfs(n_r, n_c) + 1)
    return dp[r][c]


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
print(answer)
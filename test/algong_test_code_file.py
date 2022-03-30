def dfs(f, r, c):
    stack = []
    stack.append([r, c])
    color = f[r][c]
    f[r][c] = -1
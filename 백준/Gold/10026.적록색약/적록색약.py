def dfs(f, r, c):
    stack = []
    stack.append([r, c])
    color = f[r][c]
    f[r][c] = -1

    while stack:
        now = stack.pop()
        now_r = now[0]
        now_c = now[1]

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_r = now_r + d[0]
            next_c = now_c + d[1]

            if 0 <= next_r <= (N - 1) and 0 <= next_c <= (N -1) and f[next_r][next_c] == color:
                stack.append([next_r, next_c])
                f[next_r][next_c] = -1

N = int(input())
field1 = []
field2 = [[0] * N for i in range(N)]

for i in range(N):
    field1.append(list(input()))
    for j in range(N):
        if field1[i][j] == 'G':
            field2[i][j] = 'R'
        else:
            field2[i][j] = field1[i][j]

count1 = 0
count2 = 0

for i in range(N):
    for j in range(N):
        if field1[i][j] != -1:
            dfs(field1, i, j)
            count1 += 1

for i in range(N):
    for j in range(N):
        if field2[i][j] != -1:
            dfs(field2, i, j)
            count2 += 1

print(count1, count2, sep = " ")
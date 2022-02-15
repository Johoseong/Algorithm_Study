def bfs(r, c, k):
    visited = [[[0] * (1 << 10) for i in range(20)] for j in range(20)]
    queue = []
    queue.append([[0, 0], [r, c]])
    visited[r][c][0] = 0

    while queue:
        now = queue.pop(0)
        now_d = now[0][0]
        now_k = now[0][1]
        now_r = now[1][0]
        now_c = now[1][1]

        if now_k == (1 << k) - 1:
            return now_d

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_d = now_d + 1
            next_k = now_k
            next_r = now_r + d[0]
            next_c = now_c + d[1]

            if next_r < 0 or next_c < 0 or next_r >= h or next_c >= w or m[next_r][next_c] == -1:
                continue
            if m[next_r][next_c] > 0:
                next_k |= (1 << (m[next_r][next_c] - 1))
            if visited[next_r][next_c][next_k]:
                continue
            queue.append([[next_d, next_k], [next_r, next_c]])
            visited[next_r][next_c][next_k] = 1

    return -1

m = []
result = []

while 1:
    w, h = map(int, input().split())
    field = []
    m = [[0] * 20 for i in range(20)]

    if w == 0 and h == 0:
        break
    for i in range(h):
        field.append(list(input()))

    r = 0
    c = 0
    k = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 'o':
                r = i
                c = j
                m[i][j] = 0
            elif field[i][j] == '*':
                k += 1
                m[i][j] = k
            elif field[i][j] == 'x':
                m[i][j] = -1
            else:
                m[i][j] = 0
    
    result.append(bfs(r, c, k))

for i in result:
    print(i)
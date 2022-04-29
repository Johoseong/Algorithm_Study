def selectWall(r, c, count):
    if count == 3:
        virusCount()
        return
    
    for i in range(r, N):
        for j in range(M):
            if path[i][j] == 0:
                path[i][j] = 1
                selectWall(i, j, count + 1)
                path[i][j] = 0

def virusCount():
    global maxCount
    queue = []
    virus = [[0] * M for i in range(N)]
    moveDir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for i in range(N):
        for j in range(M):
            virus[i][j] = path[i][j]

    for i in range(N):
        for j in range(M):
            if virus[i][j] == 2:
                queue.append([i, j])

    while queue:
        now = queue.pop(0)
        now_r = now[0]
        now_c = now[1]

        for d in moveDir:
            next_r = now_r + d[0]
            next_c = now_c + d[1]

            if 0 <= next_r <= (N - 1) and 0 <= next_c <= (M - 1) and virus[next_r][next_c] == 0:
                queue.append([next_r, next_c])
                virus[next_r][next_c] = 2

    count = 0
    for i in range(N):
        for j in range(M):
            if virus[i][j] == 0:
                count += 1

    if count > maxCount:
        maxCount = count

N, M = map(int, input().split())
path = [[0] * M for i in range(N)]
queue = []
maxCount = -1

for i in range(N):
    path[i] = list(map(int, input().split()))

selectWall(0, 0, 0)
print(maxCount)
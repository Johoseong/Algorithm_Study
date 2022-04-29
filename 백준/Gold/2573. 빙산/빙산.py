import sys
from collections import deque

def bfs(r, c):
    queue = deque()
    queue.append([r, c])
    visited[r][c] = 1

    while queue:
        now_r, now_c = queue.popleft()

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_r = now_r + d[0]
            next_c = now_c + d[1]

            if 0 > next_r or next_r >= N or 0 > next_c or next_c >= M or visited[next_r][next_c] == 1:
                continue
            if field[next_r][next_c] == 0:
                if tmp[now_r][now_c] == 0:
                    continue
                tmp[now_r][now_c] -= 1
            if field[next_r][next_c] > 0:
                queue.append([next_r, next_c])
                visited[next_r][next_c] = 1


def check():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and field[i][j] > 0: # 분리됐으면 걸린 시간 출력
                return 1

    for i in range(N):
        for j in range(M):
            if tmp[i][j] != 0:
                return 0 # 분리 안되고 빙산 남아있음
    return -1 # 분리 된 적 없이 빙산 다 녹음

N, M = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
tmp = [[0] * M for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        tmp[i][j] = field[i][j]

while True:
    row = 0
    col = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and field[i][j] > 0:
                row = i
                col = j
    bfs(row, col)

    c = check()
    if c == 1: # 분리됐는지 체크!!!!!!
        print(count)
        break
    elif c == -1:
        print(0)
        break

    count += 1

    for i in range(N): # 방문 배열 초기화
        for j in range(M):
            visited[i][j] = 0
            field[i][j] = tmp[i][j]
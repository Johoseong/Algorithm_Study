from collections import deque
import sys

def bfs(laser, visited):
    global result

    queue = deque([(laser[0][0], laser[0][1])])
    visited[laser[0][0]][laser[0][1]] = -1

    while queue:
        now_r, now_c = queue.popleft()

        if now_r == laser[1][0] and now_c == laser[1][1]:
            return visited[now_r][now_c]
            
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr = now_r + d[0]
            nc = now_c + d[1]
            # next_dir += 1
            while True:
                if not (0 <= nr < H and 0 <= nc < W):   # 격자 벗어나거나
                    break
                if field[nr][nc] == "*":                    # 벽 만나면 break
                    break
                if visited[nr][nc] < visited[now_r][now_c] + 1:     # 이동할 위치에 있는 거울이 현재까지 사용한 거울+1보다 작으면 갱신 X
                    break
                queue.append((nr, nc))                      # 새 위치 이동
                visited[nr][nc] = visited[now_r][now_c] + 1
                nr += d[0]
                nc += d[1]

W, H = map(int, sys.stdin.readline().split()) 
field = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
laser = []
result = 100000000
visited = [[100000000] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if field[i][j] == 'C':
            laser.append([i, j])

print(bfs(laser, visited))
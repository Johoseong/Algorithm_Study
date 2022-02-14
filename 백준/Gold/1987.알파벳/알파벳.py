import sys

def bfs():
    global ans
    queue = set([(0, 0, field[0][0])])

    while queue:
        now_r, now_c, now_list = queue.pop()
        ans = max(ans, len(now_list))

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_r = now_r + d[0]
            next_c = now_c + d[1]

            if 0 <= next_r < R and 0 <= next_c < C and field[next_r][next_c] not in now_list:
                queue.add((next_r, next_c, now_list + field[next_r][next_c]))

R, C = map(int, sys.stdin.readline().split()) 
field = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

alphabet = set()
ans = 1
bfs()
print(ans)
from collections import deque

def find(blocks, mat, isuse, answer):
    
    for index, pattern in enumerate(blocks):
        if isuse[index] == 1: continue
        for block in pattern:
            cnt = 0
            if len(mat) == len(block) and len(mat[0]) == len(block[0]):
                flag = 1
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        if mat[i][j] != block[i][j]:
                            flag = 0
                            break
                        if mat[i][j] == 1: cnt += 1
                    if flag == 0:
                        break
                if flag == 0: continue
                else:
                    isuse[index] = 1
                    return cnt, True

            continue
    return cnt, False
def rotate(mat):
    news = []
    news.append(mat)
    max_row = len(mat) - 1 
    max_col = len(mat[0]) - 1
    new1 = [[0] * (max_row + 1) for _ in range(max_col + 1)]
    new2 = [[0] * (max_col + 1) for _ in range(max_row + 1)]
    new3 = [[0] * (max_row + 1) for _ in range(max_col + 1)]

    for i in range(max_row + 1):
        for j in range(max_col + 1):
            # 1.
            new1[j][max_row - i] = mat[i][j]
            # 2.
            new2[max_row - i][max_col - j] = mat[i][j]
            # 3.
            new3[max_col - j][i] = mat[i][j]
    news.append(new1)
    news.append(new2)
    news.append(new3)
    return news

def make_matrix(max_row, max_col, min_row, min_col, block):
    mat = [[0] * (max_col + 1 - min_col) for _ in range(max_row + 1 - min_row)]
    for r, c in block:
        cr = r - min_row
        cc = c - min_col
        mat[cr][cc] = 1
    return mat

def bfs(flag, N, matrix, r, c):
    visited = [[0] * N for _ in range(N)]
    que = deque()
    que.append([r, c])
    block = []
    min_row, min_col = 51, 51
    max_row, max_col = -1, -1
    while que:
        cr, cc = que.popleft()
        visited[cr][cc] = 1
        block.append([cr, cc])
        min_row = min(min_row, cr)
        min_col = min(min_col, cc)
        max_row = max(max_row, cr)
        max_col = max(max_col, cc)

        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr = cr + d[0]
            nc = cc + d[1]

            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc] or matrix[nr][nc] == flag: continue

            que.append([nr, nc])
            matrix[nr][nc] = flag

    return max_row, max_col, min_row, min_col, block

def solution(game_board, table):
    N = len(game_board)
    answer = 0
    blocks = []

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                max_row, max_col, min_row, min_col, block = bfs(0, N, table, i, j)
                mat = make_matrix(max_row, max_col, min_row, min_col, block)
                blocks.append(rotate(mat))
    isuse = [0] * (len(blocks))
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                max_row, max_col, min_row, min_col, block = bfs(1, N, game_board, i, j)
                mat = make_matrix(max_row, max_col, min_row, min_col, block)
                cnt, f = find(blocks, mat, isuse, answer)
                
                if f: answer += cnt
                
    return answer
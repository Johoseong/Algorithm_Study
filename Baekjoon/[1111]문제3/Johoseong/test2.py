def solution(n, clockwise):
    answer = [[]]
    answer = [[0] * n for _ in range(n)]

    tmp = 1
    len_list = [(n - tmp)]
    while (tmp * 2) < n:
        len_list.append(n - (tmp * 2) - 1)
        tmp += 1
    if (n % 2) == 1:
        len_list[len(len_list) - 1] += 1

    print(len_list)
    direction = []
    start = []
    if clockwise == True:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 오 아래 왼 위
        start = [[0, 0], [0, n - 1], [n - 1, n - 1], [n - 1, 0]]
    else:
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 아래 오 위 왼
        start = [[0, 0], [n - 1, 0], [n - 1, n - 1], [0, n - 1]]
        

    for i in range(4):
        cnt = 0
        now_r = start[i][0]
        now_c = start[i][1]
        now_dir = i # direction의 인덱스

        for j in range(len(len_list)):
            for k in range(len_list[j]):
                cnt += 1
                answer[now_r][now_c] = cnt
                now_r += direction[now_dir][0]
                now_c += direction[now_dir][1]

            now_r -= direction[now_dir][0]
            now_c -= direction[now_dir][1]
            now_dir += 1
            if now_dir > 3:
                now_dir = 0
            now_r += direction[now_dir][0]
            now_c += direction[now_dir][1]
    return answer

print(solution(9, False))

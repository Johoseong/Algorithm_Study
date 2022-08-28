
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
def dfs(cur, left_cnt, right_cnt, n):
    global answer

    if left_cnt == n and right_cnt == n:
        answer.add(cur)
        return

    if left_cnt < n:
        dfs(cur + "(", left_cnt + 1, right_cnt, n)
        if left_cnt > right_cnt:
            dfs(cur + ")", left_cnt, right_cnt + 1, n)
    else:
        dfs(cur + ")", left_cnt, right_cnt + 1, n)

def solution(n):
    global answer
    answer = set()

    dfs("(", 1, 0, n)
    return len(answer)
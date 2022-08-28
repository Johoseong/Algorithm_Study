def dfs(l, r, n):
    global answer
    if l == n and r == n:
        answer += 1
        return

    if l < n:
        dfs(l + 1, r, n)
        if l > r:
            dfs(l, r + 1, n)
    else:
        dfs(l, r + 1, n)

def solution(n):
    global answer
    answer = 0
    dfs(1, 0, n)
    return answer
import sys
sys.setrecursionlimit(10 ** 8)

def dfs(now):
    for i in range(0, len(tree[now])):
        sub = tree[now][i]
        dp[sub] += dp[now]
        dfs(sub)

n, m = map(int, sys.stdin.readline().split())
superior = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)

# 직속상사에 따른 트리 구조 생성
for i in range(1, len(superior)):
    sup = superior[i]
    tree[sup].append(i + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dp[a] += b

dfs(1)

for i in range(1, n + 1):
    print(dp[i], end = ' ')
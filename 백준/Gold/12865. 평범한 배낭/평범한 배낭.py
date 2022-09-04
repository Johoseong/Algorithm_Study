import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
DP = [0] * (K + 1)

for _ in range(N):
    items.append(list(map(int, input().split())))

for W, V in items:
    for i in range(K,  W - 1, -1):
        DP[i] = max(DP[i], DP[i - W] + V)

print(DP[-1])
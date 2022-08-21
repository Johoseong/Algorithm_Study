import sys
input = sys.stdin.readline

def find(N, cur, arr):
    for i in arr:
        if not friends[cur][i]:
            return [-1]
    
    if len(arr) + 1 == K:
        for i in (arr + [cur]):
            print(i)
        exit()

    for i in range(cur, N + 1):
        if friends[cur][i]:
            find(N, i, arr + [cur])

K, N, F = map(int, input().split())
friends = [[0] * (N + 1) for _ in range(N + 1)]
answer = []

for _ in range(F):
    a, b = map(int, input().split())
    friends[a][b] = b
    friends[b][a] = a

for i in range(1, N - K + 2):
    for j in range(i, N + 1):
        if friends[i][j]:
            answer = find(N, j, [i])

print(-1)
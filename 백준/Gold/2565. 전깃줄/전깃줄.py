import sys
input = sys.stdin.readline

n = int(input())
matrix = []
dp = [0] * n
for _ in range(n):
    matrix.append(list(map(int, input().split())))

matrix.sort(key=lambda x: x[0])

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if matrix[i][1] > matrix[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
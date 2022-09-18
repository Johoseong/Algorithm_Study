import sys
input = sys.stdin.readline

n = int(input())
matrix = []
dp = [0] * (n + 1)

for i in range(n):
    matrix.append(list(map(int, input().split())))
    
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        dp[j] = max(matrix[i][j] + dp[j], matrix[i][j] + dp[j + 1])

print(dp[0])
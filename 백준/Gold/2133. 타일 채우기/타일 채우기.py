import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

if n == 1:
    print(0)
    exit()
dp[2] = 3

for i in range(4, n + 1, 2):
    dp[i] = dp[2] * dp[i - 2]
    for j in range(4, i, 2):
        dp[i] += 2 * dp[i - j] # 새로운 모양은 항상 2개씩 생겨나므로, 새로운 모양에 대해선 따로 카운트
    dp[i] += 2 # 현재 i에서의 새로운 모양도 항상 2개 씩 생김

print(dp[n])
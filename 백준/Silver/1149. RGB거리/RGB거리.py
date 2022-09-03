import sys
input = sys.stdin.readline

N = int(input())
RGB = []
for _ in range(N):
    RGB.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(3):
        if j == 0:
            RGB[i][j] = min(RGB[i][j] + RGB[i - 1][1], RGB[i][j] + RGB[i - 1][2])
        elif j == 1:
            RGB[i][j] = min(RGB[i][j] + RGB[i - 1][0], RGB[i][j] + RGB[i - 1][2])
        else:
            RGB[i][j] = min(RGB[i][j] + RGB[i - 1][0], RGB[i][j] + RGB[i - 1][1])

print(min(RGB[N - 1]))
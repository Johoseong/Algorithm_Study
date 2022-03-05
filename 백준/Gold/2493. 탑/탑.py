import sys
input = sys.stdin.readline

N = int(input())
field = list(map(int, input().split()))
stack = []
result = [0] * N

stack.append(0)
for i in range(1, N):
    now = field[i]
    while stack and  now > field[stack[-1]]:
        stack.pop()
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i)

print(" ".join(list(map(str, result))))
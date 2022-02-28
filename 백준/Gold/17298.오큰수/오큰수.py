import sys
input = sys.stdin.readline

N = int(input())
field = list(map(int, input().split()))
stack = []
result = [-1] * N

for i in range(N):
    if len(stack) == 0:
        stack.append(i)
        continue

    while field[stack[-1]] < field[i]:
        result[stack[-1]] = field[i]
        stack.pop()
        if len(stack) == 0:
            break
    
    stack.append(i)

for i in result:
    print(i, end=" ")
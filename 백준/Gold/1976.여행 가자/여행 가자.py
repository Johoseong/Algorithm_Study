import sys
sys.setrecursionlimit(10 ** 6)

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    field[root_b] = root_a

def find(a):
    if field[a] == a:
        return a
    field[a] = find(field[a])
    return field[a]

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan = list(map(int, sys.stdin.readline().split()))
field = []
root = []
flag = 1

for i in range(N + 1):
    field.append(i)

for i in range(N):
    for j in range(i, N):
        if array[i][j] == 1:
            union(i + 1, j + 1)

root = find(plan[0])
for i in range(1, M):
    cur = find(plan[i])
    if cur != root:
        flag = 0
        break

if flag == 1:
    print("YES")
else:
    print("NO")
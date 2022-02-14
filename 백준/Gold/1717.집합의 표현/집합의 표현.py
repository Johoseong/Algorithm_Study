import sys
sys.setrecursionlimit(10**6)

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

n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
field = []
for i in range(n + 1):
    field.append(i)

for i in range(m):
    if array[i][0] == 0:
        union(array[i][1], array[i][2])
    else:
        if find(array[i][1]) == find(array[i][2]):
            print("YES")
        else:
            print("NO")
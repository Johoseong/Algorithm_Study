import sys

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if parent[a] > parent[b]:
            parent[a] = parent[b]
        else:
            parent[b] = parent[a]

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

V, E = map(int, sys.stdin.readline().split())
field = []
parent = list(range(V + 1))

for _ in range(E):
    field.append(list(map(int, sys.stdin.readline().split())))

field.sort(key = lambda x: x[2])

sum = 0
for a, b, c in field:
    if find(a) != find(b):
        union(a, b)
        sum += c
print(sum)
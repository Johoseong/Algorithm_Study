import sys

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        network[root_b] = root_a
        number[root_a] += number[root_b]

def find(a):
    if a == network[a]:
        return a
    network[a] = find(network[a])
    return network[a]

n = int(sys.stdin.readline())
for i in range(n):
    F = int(sys.stdin.readline())
    network = dict()
    number = dict()

    for j in range(F):
        friend1, friend2 = sys.stdin.readline().split()
        if friend1 not in network:
            network[friend1] = friend1
            number[friend1] = 1
        if friend2 not in network:
            network[friend2] = friend2
            number[friend2] = 1

        union(friend1, friend2)
        print(number[find(friend1)])

import sys
sys.setrecursionlimit(10 ** 6)

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a == root_b:
        return
    # 친구비 더 작은거로 통일
    if price[root_a] > price[root_b]:
        price[root_a] = price[root_b]
    else:
        price[root_b] = price[root_a]

    if root_b < root_a:
        friend[root_b] = root_a
    else:
        friend[root_a] = root_b

def find(a):
    if friend[a] == a:
        return a
    # 현재노드의 루트랑 현재노드 중 친구비 더 작은 것으로 친구비 세팅
    if price[a] > price[friend[a]]:
        price[a] = price[friend[a]]
    else:
        price[friend[a]] = price[a]
    friend[a] = find(friend[a])
    return friend[a]

N, M, k = map(int, sys.stdin.readline().split())
price = [0] + list(map(int, sys.stdin.readline().split()))
array = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
friend = [i for i in range(N + 1)]
check = set()
result = 0

for i in range(M):
    union(array[i][0], array[i][1])

for i in range(1, N + 1):
    tmp = find(i)
    if tmp not in check:
        check.add(tmp)
        result += price[tmp]

if result <= k:
    print(result)
else:
    print("Oh no")
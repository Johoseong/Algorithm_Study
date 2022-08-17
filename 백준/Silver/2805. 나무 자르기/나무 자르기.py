import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
left, right = 0, max(trees)

while left <= right:
    mid = (left + right) // 2

    tree_sum = 0
    for t in trees:
        tree_sum += max(t - mid, 0)

    if tree_sum >= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)
import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, [m, v])
bag = [int(input()) for _ in range(k)]

bag.sort()

answer = 0
bag_below= []
for b in bag:
    while jewels and jewels[0][0] <= b:
        jewel = heapq.heappop(jewels)
        heapq.heappush(bag_below, -jewel[1])

    if bag_below:
        answer -= heapq.heappop(bag_below)

print(answer)
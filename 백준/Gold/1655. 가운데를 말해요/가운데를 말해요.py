import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
below, over = [], []
mid = nums[0]

for i, num in enumerate(nums):
    if i == 0:
        print(mid)
        continue

    if num < mid:
        heapq.heappush(below, -num)
    else:
        heapq.heappush(over, num)

    if len(below) > len(over):
        heapq.heappush(over, mid)
        mid = heapq.heappop(below) * (-1)
    elif len(over) - len(below) >= 2:
        heapq.heappush(below, -mid)
        mid = heapq.heappop(over)

    print(mid)
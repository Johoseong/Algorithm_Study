import heapq
import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    K = int(input())
    costs = list(map(int, input().split()))
    heap = []
    tmp = 0
    for i in range(K):
        heapq.heappush(heap, costs[i])

    while len(heap) != 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        tmp += (a + b)
        heapq.heappush(heap, a + b)
    print(tmp)

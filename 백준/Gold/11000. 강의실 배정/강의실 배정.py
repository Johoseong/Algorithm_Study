from queue import PriorityQueue
import heapq
import sys
input = sys.stdin.readline

N = int(input())
lectures = [list(map(int, input().split())) for _ in range(N)]
lectures.sort(key = lambda x:x[0])
room = 1

heap = []
heapq.heappush(heap, lectures[0][1])

for i in range(1, N):
    if lectures[i][0] < heap[0]:
        heapq.heappush(heap, lectures[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lectures[i][1])

print(len(heap))
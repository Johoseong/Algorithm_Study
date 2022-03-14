import sys
import heapq
input = sys.stdin.readline

N = int(input())
result = 0
cards = [] # heap
for _ in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result += (a + b)
    heapq.heappush(cards, a + b)
print(result)
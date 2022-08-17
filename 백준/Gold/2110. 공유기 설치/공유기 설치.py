import sys
input = sys.stdin.readline
N, C = map(int, input().split())
distance = [int(input()) for _ in range(N)]
distance.sort()
left, right = 0, max(distance)
min_dist = min(distance)
l = right - min_dist

while left <= right:
    mid = (left + right) // 2

    if mid * (C - 1) > l:
        right = mid - 1
        continue
    cnt, prev = 1, min_dist
    for i in range(1, N):
        if (distance[i] - prev) >= mid:
            cnt += 1
            prev = distance[i]
    
    if cnt >= C: # 되는 경우
        left = mid + 1
    else: # 안되는 경우
        right = mid - 1

print(right)
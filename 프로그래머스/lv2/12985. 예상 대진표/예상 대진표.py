from collections import deque
import math
# def make_square(n):    
#     a = 2
#     cnt = 1
#     while a != n:
#         a = a * 2
#         cnt += 1
#     return cnt

def solution(n,a,b):
    answer = 0
    ranges = deque()
    for i in range(1, n, 2):
        ranges.append([i, i + 1])
    
    while ranges:
        s1, e1 = ranges.popleft()
        if s1 <= a <= e1 and s1 <= b <= e1:
            # return make_square(e1 - s1 + 1)
            return int(math.log2(e1 - s1 + 1))
        s2, e2 = ranges.popleft()
        if s2 <= a <= e2 and s2 <= b <= e2:
            # return make_square(e2 - s2 + 1)
            return int(math.log2(e2 - s2 + 1))

        ranges.append([min(s1, s2), max(e1, e2)])
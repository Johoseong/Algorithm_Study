import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())
nums.sort()

negative = []
positive = []
for i in range(n):
    if nums[i] > 0:
        positive.append(nums[i])
    else:
        negative.append(nums[i])

answer = 0
i = 0
while i < len(negative) - 1:
    answer += (negative[i] * negative[i + 1])
    i += 2
answer += sum(negative[i:])

i = len(positive) - 1
while i > 0:
    if positive[i] == 1 or positive[i - 1] == 1:
        break
    answer += (positive[i] * positive[i - 1])
    i -= 2
answer += sum(positive[:i + 1])
print(answer)
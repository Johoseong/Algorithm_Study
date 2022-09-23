import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0

l = int(1e9)
sub_total = arr[end]

while start <= end:
    if sub_total < S:
        end += 1
        if end <= N - 1:
            sub_total += arr[end]
        else: break
    else:
        l = min(l, end - start + 1)
        sub_total -= arr[start]
        start += 1

print(l if l != int(1e9) else 0)
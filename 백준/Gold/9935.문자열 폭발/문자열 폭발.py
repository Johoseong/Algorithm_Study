import sys
input = sys.stdin.readline

arr = list(input().rstrip())
word = list(input().rstrip())
stack = []

for i in range(len(arr)):
    stack.append(arr[i])
    if stack[-1] == word[-1] and len(stack) >= len(word):
        if stack[-len(word):] == word:
            for i in range(len(word)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
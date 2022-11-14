import sys
input = sys.stdin.readline

def insert(root, num):
    cur = root

    for n in num:
        if n not in cur:
            cur[n] = {}
        cur = cur[n]
    cur["-"] = num # 끝 표시

def search(root, num):
    cur = root
    for n in num:
        if n in cur:
            cur = cur[n]
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = []
    
    root = dict()
    for _ in range(n):
        numbers.append(input().rstrip())

    numbers.sort(key=lambda x: (-len(x)))

    flag = True
    for num in numbers:
        if search(root, num):
            flag = False
            break
        insert(root, num)

    if flag:
        print("YES")
    else:
        print("NO")
import sys
from teflib import tgraph


def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    tree = [[] for _ in range(n)]
    bosses = [int(x) for x in sys.stdin.readline().split()]
    for employee, boss in enumerate(bosses):
        if boss != -1:
            tree[boss - 1].append(employee)    
    praises = [0] * n
    for _ in range(m):
        i, w = [int(x) for x in sys.stdin.readline().split()]
        praises[i - 1] += w
        
    stack = []
    for employee in tgraph.dfs(tree, 0, stack=stack):
        if employee != 0:
            boss = stack[-2]
            praises[employee] += praises[boss]            

    print(*praises)
    
    
if __name__ == '__main__':
    main()
from collections import deque
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    
    while A:
        if B[-1] > A[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            A.pop()

    return answer
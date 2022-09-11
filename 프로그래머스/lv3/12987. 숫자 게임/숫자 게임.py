def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    while A:
        if B[-1] > A[-1]:
            answer += 1
            A.pop()
            B.pop()
        else:
            A.pop()

    return answer
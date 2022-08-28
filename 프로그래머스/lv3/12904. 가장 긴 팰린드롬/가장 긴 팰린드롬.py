def solution(s):
    answer = 1
    N = len(s)

    for center in range(1, N - 1):
        l, r = center - 1, center + 1
        cnt = 0
        while True:
            if l < 0 or r >= N: break

            if s[l] == s[r]:
                cnt += 2
                l -= 1
                r += 1
            else: break
        if cnt != 0: cnt += 1
        answer = max(answer, cnt)

    for center in range(1, N):
        l, r = center - 1, center
        cnt = 0
        while True:
            if l < 0 or r >= N: break

            if s[l] == s[r]:
                cnt += 2
                l -= 1
                r += 1
            else: break
        answer = max(answer, cnt)

    return answer
def solution(s):
    answer = [0, 0] # 횟수, 0 개수

    while s != '1':
        tmp = ''
        for i in s: # 1. 0 제거
            if i == '0':
                answer[1] += 1
                continue
            tmp += i

        l = len(tmp)
        s = format(l, 'b')
        answer[0] += 1

    return answer
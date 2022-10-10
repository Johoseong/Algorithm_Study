def convert(n, k):
    tmp = n
    convert_num = ''
    while True:
        if tmp < k:
            convert_num = str(tmp) + convert_num
            break
        leaves = tmp % k
        tmp = tmp // k
        convert_num = str(leaves) + convert_num
    return convert_num

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0    
    number = convert(n, k)
    tmp = number.split('0')

    for t in tmp:
        if t and is_prime(int(t)):
            answer += 1

    return answer
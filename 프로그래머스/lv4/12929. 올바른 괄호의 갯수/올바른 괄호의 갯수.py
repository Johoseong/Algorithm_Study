from math import factorial as f
def solution(n):
    return f(2*n)//(f(n)**2*(n+1))
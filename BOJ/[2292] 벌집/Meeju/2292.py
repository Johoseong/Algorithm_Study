def main2():
    num=int(input())
    repeat(num,1)



def repeat(n,cnt):
    n-=6*cnt
    cnt += 1
    if n>1:
        repeat(n,cnt)
    else:
        print(cnt)
    return

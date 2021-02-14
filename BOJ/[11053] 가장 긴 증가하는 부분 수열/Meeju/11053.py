import sys

def lis(arr):
    if not arr:
        return 0
    ret=1
    for i in range(len(arr)):               #이중 for문 첫번째 for문은 i가 수열의 첫번째라고 생각하고 시작하기 위함 
                                            #두번째 for문은 i가 첫번재인 for문에 대해서 i보다 큰 숫자를 nxt리스트에 저장해서 최대 ret를 구하기 위함
        nxt=[]
        for j in range(i+1,len(arr)):
            if arr[i] <arr[j]:
                nxt.append(arr[j])
        ret=max(ret,1+lis(nxt))             
    return ret

def main():
    count = sys.stdin.readline()     
    num_list = sys.stdin.readline().split()
    num_list = list(map(int, num_list))       #입력값 한줄로 받아들여서 정수로 변환후 list로 저장
    print(lis(num_list))                      #lis 함수 호출  -> 반환값 가장 긴 길이
main()

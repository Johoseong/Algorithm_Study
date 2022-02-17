from sys import stdin

def getParent(x):
    if parent_dict[x] == x:
        return x
    parent_dict[x] = getParent(parent_dict[x])
    return parent_dict[x]

def unionParent1(a, b):
    a = getParent(a)
    b = getParent(b)
    sum = cnt_dict[a] + cnt_dict[b]
    cnt_dict[a] = sum
    cnt_dict[b] = sum
    #더 작은 쪽을 부모로 갖는다
    if a > b:
        parent_dict[a] = b
    else:
        parent_dict[b] = a
    return

def unionParent2(a, b): #a가 b의 부모인 것을 전제로 할 때
    a = getParent(a)
    b = getParent(b)
    if a != b:
        parent_dict[b] = a
        cnt_dict[a] += cnt_dict[b]
    return

t = int(stdin.readline()) #number of test cases
for i in range(t):
    f = int(stdin.readline()) #number of friendships formed
    #부모를 저장하는 딕셔너리와 같은 네트워크 친구 수를 저장하는 딕셔너리
    parent_dict, cnt_dict = dict(), dict()
    for j in range(f):
        name1, name2 = stdin.readline().split()
        #입력받은 이름이 딕셔너리에 없는 경우 저장
        if name1 not in parent_dict:
            parent_dict[name1] = name1
            cnt_dict[name1] = 1
        if name2 not in parent_dict:
            parent_dict[name2] = name2
            cnt_dict[name2] = 1
        #부모를 합친다
        unionParent2(name1, name2)
        #unionParent1(name1, name2) 이 함수를 이용하면 출력초과가 뜬다

        #같은 네트워크의 친구 수를 출력
        print(cnt_dict[getParent(name1)])
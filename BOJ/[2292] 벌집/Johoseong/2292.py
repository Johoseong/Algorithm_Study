n = int(input())
arr = [1]
count = 0

i = 6
while arr[-1] <= 1000000000:
    arr.append(i + arr[-1]) #list[-1] : 배열의 마지막 원소 값
    i = i + 6

for i in arr:
    if n > i:
        count = count + 1
    else:
        break

print(count + 1)

N = int(input())

cnt = 0

while 2**cnt <= N:
    print(2**cnt, end=' ')
    cnt += 1


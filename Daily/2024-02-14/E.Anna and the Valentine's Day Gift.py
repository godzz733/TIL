
for _ in range(int(input())):
    n,m = map(int, input().split())
    t = list(map(int, input().split()))
    cnt = -1
    arr = []
    for i in t:
        tt = str(i)
        cnt += len(tt)
        num = 0
        for i in tt[::-1]:
            if i != '0':
                break
            num += 1
        arr.append((num,tt))
    arr.sort(key=lambda x: x[0])
    for i in range(len(arr)):
        if i % 2:
            arr.pop()
        else:
            cnt -= arr.pop()[0]
    print('Sasha') if cnt >= m else print('Anna')

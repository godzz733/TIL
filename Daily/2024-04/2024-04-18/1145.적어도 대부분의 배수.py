arr = list(map(int, input().split()))
ans = 1
for i in range(1,100000000):
    tem = 0
    for j in arr:
        if i % j == 0:
            tem += 1
    if tem >= 3:
        print(i)
        break
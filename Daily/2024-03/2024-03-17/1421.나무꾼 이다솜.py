n,m,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

ans = 0
for i in range(1,max(arr)+1):
    cnt = 0
    for j in arr:
        t = 0
        if j < i:
            continue
        t += (j//i)*i * k
        if j == i:
            pass
        elif not j%i:
            t -= (j//i - 1) * m
        else:
            t -= j//i * m
        if t <= 0: continue
        cnt += t
    ans = max(ans, cnt)
print(ans)
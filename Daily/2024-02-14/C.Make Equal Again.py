for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    t = arr[0]
    cnt = 0
    cnt2 = 0
    for i in range(n):
        if arr[i] != t:
            break
        cnt += 1
    if cnt == n:
        print('0')
        continue
    if arr[-1] != t:
        t = arr[-1]
        for j in range(n-1, -1, -1):
            if arr[j] != t:
                break
            cnt2 += 1
        cnt = max(cnt, cnt2)
        print(n-cnt)
        continue
    for j in range(n-1, -1, -1):
        if arr[j] != t:
            break
        cnt2 += 1
    print(n-(cnt+cnt2))
import sys; I = sys.stdin.readline
n = int(I())
arr = list(map(int, I().split()))
s = int(I())
ans = sorted(arr)[::-1]
if s >= n**2:
    print(*ans)
else:
    an = []
    while s and arr:
        t = max(arr[:s+1])
        i = arr.index(t)
        arr = arr[:i] + arr[i+1:]
        an.append(t)
        s -= i
    arr = an + arr
    print(*arr)
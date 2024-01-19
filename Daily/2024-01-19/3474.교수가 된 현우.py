import sys; I = sys.stdin.readline
arr = [1]
for i in range(1,16):
    arr.append(arr[i-1]*5 + 1)
for _ in range(int(I())):
    n = int(I())
    ans = 0
    while n >= 5:
        t = 1
        idx = -1
        while 1:
            t *= 5
            if t > n:
                t //= 5
                break
            idx += 1
        n -= t
        ans += arr[idx]
    print(ans)
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
def make_arr(x):
    return [arr[i][x] for i in range(n)]
def check():
    t = 0
    if m:
        for i in range(n):
            if sum(arr[i]) > n//2:
                t += 1
        if t > n//2:
            print(1)
            exit()
        t = 0
        for i in range(m):
            if sum(make_arr(i)) > n//2:
                t += 1
        if t > n//2:
            print(1)
            exit()
    else:
        for i in range(n):
            if sum(arr[i]) <= n//2:
                t += 1
        if t > n//2:
            print(1)
            exit()
        t = 0
        for i in range(m):
            if sum(make_arr(i)) < n // 2:
                t += 1
        if t > n//2:
            print(1)
            exit()
if m:
    for _ in range(n):
        for i in range(n):
            if sum(arr[i]) > n//2:
                arr[i] = [1 for _ in range(n)]
        for i in range(n):
            if sum(make_arr(i)) > n//2:
                for j in range(n):
                    arr[j][i] = 1
        check()
else:
    for _ in range(n):
        for i in range(n):
            if sum(arr[i]) <= n//2:
                arr[i] = [0 for _ in range(n)]
        for i in range(n):
            if sum(make_arr(i)) <= n//2:
                for j in range(n):
                    arr[j][i] = 0
        check()
print(0)
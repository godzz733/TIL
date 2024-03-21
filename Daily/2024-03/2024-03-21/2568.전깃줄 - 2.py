import sys; input = sys.stdin.readline
def binary(x, start, end, size):
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < x:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    if start == size:
        return -1
    return res


n = int(input())
tem = []
for _ in range(n):
    tem.append(tuple(map(int, input().split())))
tem.sort()
dp = [0] * 500001
arr = [-1] * 500001
for x,y in tem:
    arr[x] = 0
size = 0
for x,y in tem:
    t = binary(y, 0, size, size + 1)
    if t == -1:
        dp[size] = y
        arr[x] = size + 1
        size += 1
    else:
        dp[t] = y
        arr[x] = t + 1
ans = []
for i in range(tem[-1][0], 0, -1):
    if arr[i] == size:
        size -= 1
    elif arr[i] != -1:
        ans.append(i)
print(len(ans))
for i in range(len(ans) - 1, -1, -1):
    print(ans[i])
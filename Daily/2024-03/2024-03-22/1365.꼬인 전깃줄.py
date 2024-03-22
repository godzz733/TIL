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
tem = list(map(int,input().split()))
dp = [0] * (n+1)
size = 0
for i in range(n):
    t = binary(tem[i], 0, size, size + 1)
    if t == -1:
        dp[size] = tem[i]
        size += 1
    else:
        dp[t] = tem[i]
print(n - size)
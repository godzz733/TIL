import sys; I = sys.stdin.readline
n = int(I())
arr = [int(I()) for _ in range(n)]
m = max(arr)
r = [0] * (m+1)
for i in arr:
    r[i] += 1
ans = [-1] * (m+1)
for i in sorted(list(set(arr))):
    for j in range(i, m+1, i):
        ans[j] += r[i]
for i in arr:
    print(ans[i])
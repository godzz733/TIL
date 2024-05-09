import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'Y': arr[i][j] = 1
        else: arr[i][j] = 0

p = [i for i in range(n)]
ans = [0] * n

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
cnt = 0
for i in range(n):
    for j in range(n):
        if cnt == m:
            print(*ans)
            exit()
        if arr[i][j]:
            if find(i) != find(j):
                union(i,j)
                cnt += 1
                ans[i] += 1
                ans[j] += 1
                arr[i][j] = 0
                arr[j][i] = 0
t = find(0)
for i in range(1,n):
    if find(i) != t:
        print(-1)
        exit()

for i in range(n):
    for j in range(n):
        if cnt == m:
            print(*ans)
            exit()
        if arr[i][j]:
            ans[i] += 1
            ans[j] += 1
            arr[j][i] = 0
            cnt += 1
print(-1)
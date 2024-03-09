import sys; input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n):
    t = list(map(int, input().split()))
    for i in range(1, len(t)-1, 2):
        arr[t[0]].append((t[i], t[i+1]))
dis = [int(1e9)] * (n+1)
dis[1] = 0
v = set()
q = [1]
v.add(1)
while q:
    x = q.pop()
    for i, j in arr[x]:
        if i not in v:
            v.add(i)
            dis[i] = dis[x] + j
            q.append(i)

idx = dis.index(max(dis[1:]))

dis = [int(1e9)] * (n+1)
dis[idx] = 0
v = set()
q = [idx]
v.add(idx)
while q:
    x = q.pop()
    for i, j in arr[x]:
        if i not in v:
            v.add(i)
            dis[i] = dis[x] + j
            q.append(i)
print(max(dis[1:]))
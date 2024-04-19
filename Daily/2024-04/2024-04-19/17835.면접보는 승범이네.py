import sys; input = sys.stdin.readline
import heapq as h

n,m,k = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    arr[b].append((a,c))

d = [int(1e12)] * (n+1)
q = []
for i in map(int, input().split()):
    d[i] = 0
    h.heappush(q, (0, i))

while q:
    dist, now = h.heappop(q)
    if d[now] < dist:
        continue
    for x,y in arr[now]:
        cost = dist + y
        if d[x] > cost:
            d[x] = cost
            h.heappush(q, (cost, x))
ans = max(d[1:])
print(d.index(ans))
print(ans)
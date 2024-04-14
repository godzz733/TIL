import sys; input = sys.stdin.readline
import heapq as h
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
moving = []
for _ in range(m):
    a,b,c = map(int, input().split())
    moving.append((a,b))
    arr[a].append((b,c))
    arr[b].append((a,c<<1))

d = [0,0] + [int(1e12)]*(n-1)

q = []
h.heappush(q, (0, 1))

while q:
    dist, now = h.heappop(q)
    if d[now] < dist: continue
    for x,y in arr[now]:
        cost = y + d[now]
        if cost < d[x]:
            d[x] = cost
            h.heappush(q,(cost,x))
print(sum(d[1:]))
for x,y in moving:
    if d[x] < d[y]:
        print("1",end=" ")
    else:
        print("0", end=" ")
import sys; input = sys.stdin.readline
import heapq as h
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
V = [int(1e9)]*(n+1)
st,fi = map(int, input().split())
V[st] = 0
test = [0] * (n+1)
q = []
h.heappush(q, (0,st))
while q:
    dist, now = h.heappop(q)
    if V[now] < dist: continue
    for next, cost in arr[now]:
        next_cost = dist + cost
        if next_cost < V[next]:
            V[next] = next_cost
            test[next] = now
            h.heappush(q, (next_cost, next))
print(V[fi])
ans = [fi]
now = fi
while now != st:
    now = test[now]
    ans.append(now)
print(len(ans))
print(*ans[::-1])
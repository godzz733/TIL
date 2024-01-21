import sys; I = sys.stdin.readline
import heapq as h
n,m = map(int,I().split())
arr = [*map(int,I().split())]
q = []
s = 0
ans = 0
for i in arr:
    s += i
    h.heappush(q,-i)
    if s >= m:
        s += h.heappop(q) * 2
        ans += 1
print(ans)
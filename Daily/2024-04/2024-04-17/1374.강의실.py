import sys; input = sys.stdin.readline
import heapq as h
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
q = []
arr.sort(key=lambda x: x[1])
for a,b,c in arr:
    if not q:
        h.heappush(q, c)
    else:
        x= h.heappop(q)
        if x <= b:
            pass
        else:
            h.heappush(q, x)
        h.heappush(q, c)
print(len(q))
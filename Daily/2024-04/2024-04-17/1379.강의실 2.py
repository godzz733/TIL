import sys; input = sys.stdin.readline
import heapq as h
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
q = []
ans = [0] * (n+1)
num = 1
arr.sort(key=lambda x: x[1])
for a,b,c in arr:
    if not q:
        ans[a] = 1
        h.heappush(q, (c,b,1))
    else:
        x,y,z = h.heappop(q)
        if x <= b:
            ans[a] = z
        else:
            h.heappush(q, (x,y,z))
            ans[a] = len(q)+1
        h.heappush(q, (c,b,ans[a]))
print(len(q))
for i in range(1,n+1): print(ans[i])
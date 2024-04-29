import sys; input = sys.stdin.readline
from itertools import permutations
n,m,k,t,p = map(int, input().split())
arr = []
for _ in range(k):
    a,b,c = map(int, input().split())
    arr.append((a,b,c))
ans = [0,0]
for i in permutations(arr, k):
    a,b,c = i[0]
    tem = 1
    time = t
    for x,y,z in i[1:]:
        if abs(a-x) + abs(b-y) <= time:
            time -= abs(a-x) + abs(b-y)
            tem += 1
            a,b,c = x,y,z
        else:
            break
    ans[0] = max(ans[0], tem)
for i in range(1,n+1):
    for j in range(1,m+1):
        tem = 0
        for a,b,c in arr:
            if a == i and b == j:
                tem += 1
                continue
            if p/(abs(i-a) + abs(j-b)) >= c:
                tem += 1
        ans[1] = max(ans[1], tem)
print(*ans)
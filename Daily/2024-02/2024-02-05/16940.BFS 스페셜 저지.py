import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
arr = [[] for _ in range(n+1)]
lst = [0,1] + [0] * n
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = list(map(int, input().split()))
if ans[0] != 1:
    print(0)
    exit()
_set = set()
_set.add(1)

q = deque([1])
while q:
    x = q.popleft()
    for i in arr[x]:
        if i not in _set:
            lst[i] = lst[x] + 1
            _set.add(i)
            q.append(i)
_max = max(lst)
idx = 0
cnt = 1
t = [0] * (_max+1)
for i in lst:
    t[i] += 1
idx = 0
cnt = 1
while cnt < _max:
    z = idx+t[cnt]
    for i in range(idx,idx+t[cnt]):
        c = 0
        while c<len(arr[ans[i]])-1 and z <= idx+t[cnt]+t[cnt+1]-1:
            if ans[z] not in arr[ans[i]]:
                print(0)
                exit()
            z += 1
            c += 1
    idx += t[cnt]
    cnt += 1
print(1)
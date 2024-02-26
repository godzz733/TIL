import sys; input = sys.stdin.readline
from itertools import permutations
n = int(input())
t = [input().rstrip() for _ in range(n)]
arr = {}
head = set()
disable = set()
for i in t:
    head.add(i[0])
    for j in range(len(i)):
        arr[i[j]] = arr.get(i[j],0) + 10**(len(i)-j-1)
arr = sorted(arr.items(), key=lambda x: -x[1])
ans = 0
if len(arr) < 10:
    for i in range(len(arr)):
        ans += (9-i)*arr[i][1]
    print(ans)
else:
    for i in range(len(arr)):
        if arr[i][0] in head:
            disable.add(i)
    for i in permutations([x for x in range(10)],10):
        tem = 0
        for j in range(10):
            tem += arr[j][1]*i[j]
            if not i[j] and j in disable:
                break
        else:
            ans = max(ans,tem)
    print(ans)
import sys; input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    n = int(input())
    arr = []
    lst = [[] for _ in range(n)]
    home = tuple(map(int, input().split()))
    for _ in range(n):
        arr.append(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))
    ans = set([])
    for i in range(n):
        if (abs(festival[0] - arr[i][0]) + abs(festival[1] - arr[i][1])) <= 1000:
            ans.add(i)
        for j in range(n):
            if i != j:
                if (abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1])) <= 1000:
                    lst[i].append(j)
    q = deque()
    v = [False] * n
    for i in range(n):
        if (abs(arr[i][0] - home[0]) + abs(arr[i][1] - home[1])) <= 1000:
            q.append(i)
            v[i] = True
    if abs(home[0] - festival[0]) + abs(home[1] - festival[1]) <= 1000:
        print("happy")
        continue
    while q:
        cur = q.popleft()
        if cur in ans:
            print("happy")
            break
        for i in lst[cur]:
            if not v[i]:
                v[i] = True
                q.append(i)
    else:
        print("sad")
import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
num = {}
for i in range(n):
    num[arr[i]] = num.get(arr[i], 0) + 1
q = []
ans = [-1] * n
for i in range(n):
    print(q)
    if not q:
        q.append((i, num[arr[i]]))
    else:
        while q:
            idx, cnt = q.pop()
            if cnt < num[arr[i]]:
                ans[idx] = arr[i]
            else:
                q.append((idx, cnt))
                break
        q.append((i, num[arr[i]]))
print(*ans)
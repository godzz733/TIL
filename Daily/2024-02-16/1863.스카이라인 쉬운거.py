import sys; input = sys.stdin.readline
n = int(input())
ans = 0
arr = []
for i in range(n):
    a,b = map(int, input().split())
    if not b:
        ans += len(arr)
        arr = []
        continue
    if not arr:
        arr.append(b)
    else:
        if arr[-1] == b:
            continue
        elif arr[-1] < b:
            arr.append(b)
        else:
            while arr and arr[-1] > b:
                ans += 1
                arr.pop()
            if arr and arr[-1] == b:
                continue
            else:
                arr.append(b)
if arr:
    ans += len(arr)
print(ans)
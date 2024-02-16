import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [[0,987654321] for _ in range(n)]
lst = []
for i in range(n):
    if not lst:
        lst.append((arr[i],i+1))
    else:
        while lst and lst[-1][0] <= arr[i]:
            lst.pop()
        if lst:
            ans[i][0] += len(lst)
            ans[i][1] = lst[-1][1]
        lst.append((arr[i],i+1))
lst.clear()
for i in range(n-1,-1,-1):
    if not lst:
        lst.append((arr[i],i+1))
    else:
        while lst and lst[-1][0] <= arr[i]:
            lst.pop()
        if lst:
            ans[i][0] += len(lst)
            if abs(lst[-1][1]-i-1) < abs(ans[i][1]-i-1):
                ans[i][1] = lst[-1][1]
        lst.append((arr[i],i+1))
for i in range(n):
    if not ans[i][0]:
        print(0)
        continue
    print(*ans[i])
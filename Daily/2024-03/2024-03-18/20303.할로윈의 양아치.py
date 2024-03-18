import sys; input = sys.stdin.readline
n,m,k = map(int, input().split())
lst = list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
friends = []
ans = [0] * 3001
v = [0] * 30001
def check(x):
    cnt = lst[x-1]
    l = 1
    v[x] = 1
    tarr = [x]
    while tarr:
        x = tarr.pop()
        for i in arr[x]:
            if not v[i]:
                v[i] = 1
                l += 1
                tarr.append(i)
                cnt += lst[i-1]
    return (cnt,l)
for i in range(1,n+1):
    if not v[i]:
        friends.append(check(i))
for x,y in friends:
    for i in range(k,-1,-1):
        if i >= y:
            ans[i] = max(ans[i],ans[i-y]+x)
        else:
            break
print(max(ans[:k]))
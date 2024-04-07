import sys; input = sys.stdin.readline
n,m = map(int,input().split())
ans = 0
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    if a >= b: ans += 1
    else:
        arr.append(a)
arr.sort(reverse=True)
while arr:
    ans += 1
    arr.pop()
    tem = m-1
    while arr and tem > 0:
        a = arr.pop()
        if tem < a:
            if not arr:
                ans += 1
                print(ans)
                exit()
            c = arr.pop()
            arr.append(c-tem)
            arr.append(a)
            break
        tem -= a
print(ans)
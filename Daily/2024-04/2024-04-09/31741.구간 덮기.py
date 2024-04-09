import sys; input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [[],[],[]]
ans = int(1e10)
for _ in range(n):
    a,b = map(int, input().split())
    if a <= l and b >= r:
        print(0)
        exit()
    if b < l or a > r:
        continue
    if a <= l:
        arr[0].append(b)
    elif b >= r:
        arr[2].append(a)
    else:
        arr[1].append((a,b))
if not arr[0] or not arr[2]:
    print(-1)
    exit()
arr[0].sort()
arr[2].sort()

def bisect1(y):
    global ans
    st = 0
    fi = len(arr[2]) - 1
    res = 0
    while st <= fi:
        mid = (st + fi) // 2
        if arr[2][mid]> y:
            fi = mid - 1
        else:
            st = mid + 1
            res = arr[2][mid]
    if not res:
        return
    ans = min(ans, abs(y - res))
def bisect2(x,y):
    global ans
    st = 0
    fi = len(arr[0]) - 1
    res = 0
    tem = 0
    while st <= fi:
        mid = (st + fi) // 2
        if arr[0][mid] < x:
            st = mid + 1
        else:
            fi = mid - 1
            res = arr[0][mid]
    if not res:
        return
    tem += abs(res - x)
    st = 0
    fi = len(arr[2]) - 1
    res = 0
    while st <= fi:
        mid = (st + fi) // 2
        if arr[2][mid] > y:
            fi = mid - 1
        else:
            st = mid + 1
            res = arr[2][mid]
    if not res:
        return
    tem += abs(y - res)
    ans = min(ans, tem)

for x in arr[0]:
    bisect1(x)
for x,y in arr[1]:
    bisect2(x,y)
ans = -1 if ans == int(1e10) else ans
print(ans)
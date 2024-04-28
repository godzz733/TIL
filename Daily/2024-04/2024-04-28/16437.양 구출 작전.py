import sys; input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
lst = [0] * (n+1)
for i in range(n-1):
    a,b,c = map(str,input().split())
    b = int(b)
    c = int(c)
    if a == 'S':
        arr[c].append(i+2)
        lst[i+2] = b
    else:
        arr[c].append(i+2)
        lst[i+2] = -b

V = [0]*(n+1)
def check(x):
    global ans
    if V[x] == 1:
        return ans[x]
    V[x] = 1
    for a in arr[x]:
        lst[x] += check(a)
    return lst[x] if lst[x] >= 0 else 0
check(1)
print(lst[1])

import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,r,q = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
num = [1] * (n+1)
v = [0]*(n+1)
def tree(x):
    if v[x]: return num[x]
    v[x] = 1
    for i in arr[x]:
        if v[i]: continue
        num[x] += tree(i)
    return num[x]
tree(r)
for _ in range(q):
    x = int(input())
    print(num[x])
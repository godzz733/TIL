import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr = [[] for _ in range(n+1)]
parent = [[0] * 21 for _ in range(n+1)]
level = [0] * (n+1)
v = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def set_parent(x, cnt):
    v[x] = 1
    level[x] = cnt
    for i in arr[x]:
        if not v[i]:
            parent[i][0] = x
            set_parent(i, cnt+1)

def solve():
    set_parent(1, 0)
    for i in range(1, 21):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a,b):
    if level[a] > level[b]:
        a, b = b, a
    
    for i in range(20, -1, -1):
        if level[b] - level[a] >= (1 << i):
            b = parent[b][i]
    
    if a == b:
        return a
    for i in range(20,-1,-1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

solve()

m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))
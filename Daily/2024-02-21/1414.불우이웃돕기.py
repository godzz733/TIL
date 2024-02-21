import sys; input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
lst = []
ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == '0': arr[i][j] =0
        elif arr[i][j].islower() :arr[i][j] = ord(arr[i][j])-ord('a')+1
        else: arr[i][j] = ord(arr[i][j])-ord('A')+27
        if arr[i][j] != 0: lst.append((arr[i][j],i,j))
    
for i in range(n): ans += sum(arr[i])

parent = [i for i in range(n)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b: parent[b] = a
    else: parent[a] = b

lst.sort()
for i in lst:
    cost,a,b = i
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        ans -= cost
for i in range(n):
    parent[i] = find_parent(i)
if sum(parent) != 0: ans = -1
print(ans)
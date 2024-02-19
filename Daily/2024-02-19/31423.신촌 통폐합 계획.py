import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
lst = [input().rstrip() for _ in range(n)]
arr = [[] for _ in range(n+1)]
st = 0
for i in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    if i == n-2:
        st = a
print(lst[st-1], end = '')
def ans(x):
    for i in arr[x]:
        print(lst[i-1], end = '')
        ans(i)
ans(st)
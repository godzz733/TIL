import sys; input = sys.stdin.readline
from itertools import permutations
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

ans = 987654321
t = [i for i in range(n)]
t.remove(m)
for i in permutations(t, n-1):
    temp = 0
    temp += arr[m][i[0]]
    for j in range(n-2):
        temp += arr[i[j]][i[j+1]]
        if temp > ans:
            break
    ans = min(ans, temp)
print(ans)
import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
arr = [[0] * (2*n + 1) for _ in range(n+1)]
for i in range(2*n+1):
    for j in range(n+1):
        if i <= n:
            if i < j:
                arr[j][i] = -1
        else:
            if 2 * n - i < j:
                arr[j][i] = -1
arr = arr
ans = [[0] * (2*n + 1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[b][a] = -1
if arr[0][2*n] == -1:
    print(-1)
    exit() 
# for _ in range(n+1):
#     print(arr[_])
dx = [1,1]
dy = [1,-1]
q = deque()
q.append((0,0))
while q:
    x,y = q.popleft()
    for i in range(2):
        nx,ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > 2*n or ny < 0 or ny > n:
            continue
        if arr[ny][nx] == -1:
            continue
        if ans[ny][nx] == 0:
            ans[ny][nx] = 1
            q.append((nx,ny))
dx = [-1,-1]
dy = [1,-1]
q = deque()
q.append((2*n,0))
while q:
    x,y = q.popleft()
    for i in range(2):
        nx,ny = x + dx[i], y + dy[i]
        if nx < 0 or nx > 2*n or ny < 0 or ny > n:
            continue
        if arr[ny][nx] == -1:
            continue
        if ans[ny][nx] == 0:
            ans[ny][nx] = 2 
            q.append((nx,ny))
        if ans[ny][nx] == 1:
            ans[ny][nx] = 3
            q.append((nx,ny))
# for _ in range(n+1):
#     print(ans[_])
for i in range(n,-1,-1):
    for j in range(2*n+1):
        if ans[i][j] == 3:
            print(i)
            exit()
print(-1)
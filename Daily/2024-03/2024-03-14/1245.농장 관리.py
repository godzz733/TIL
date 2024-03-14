import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,-1,-1,1]
V = [[0]*m for _ in range(n)]
def check(x,y):
    if V[x][y]:
        return False
    q = deque()
    q.append((x,y))
    v = set()
    v.add((x,y))
    V[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == arr[x][y] and not V[nx][ny]:
                q.append((nx,ny))
                V[nx][ny] = 1
                v.add((nx,ny))
    for x,y in v:
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] not in v:
                if arr[nx][ny] > arr[x][y]:
                    return False
    return True
ans = 0
for i in range(n):
    for j in range(m):
        if check(i,j):
            ans += 1
print(ans)
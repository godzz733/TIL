import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def find_ans(x,y):
    global v
    if v[x][y] or arr[x][y] == 0:
        return False
    q = deque()
    q.append((x,y))
    v[0][0] = True
    while q:
        x,y = q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if not v[nx][ny] and arr[nx][ny] != 0:
                    v[nx][ny] = True
                    q.append((nx,ny))
    return True

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            q.append((i,j,arr[i][j]))
ans = 0        
while 1:
    ans += 1
    tarr = []
    while q:
        x,y,cnt = q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 0:
                    cnt -= 1
        if cnt > 0:
            tarr.append((x,y,cnt))
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for x,y,cnt in tarr:
        arr[x][y] = cnt
    t = 0 
    v = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if find_ans(i,j):
                t += 1
    if t >= 2:
        print(ans)
        break
    if t == 0:
        print(0)
        break
    q = deque(tarr)
else:
    print(0)
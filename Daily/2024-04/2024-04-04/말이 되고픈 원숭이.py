import sys; input = sys.stdin.readline
from collections import deque
k = int(input())
m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

dx2 = [2,2,1,1,-1,-1,-2,-2]
dy2 = [1,-1,2,-2,2,-2,1,-1]

dp = [[[987654321]*m for _ in range(n)] for _ in range(k+1)]

q = deque()
for i in range(k+1):dp[i][0][0] = 0
# x,y,k,cnt
q.append((0,0,0,0))
ans = -1
while q:
    x,y,num,cnt = q.popleft()
    if x == n-1 and y == m-1:
        ans = cnt
        break
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] == 1:continue
            if dp[num][nx][ny] > cnt + 1:
                dp[num][nx][ny] = cnt + 1
                q.append((nx,ny,num,cnt+1))
    if num < k:
        for i in range(8):
            nx,ny = x+dx2[i],y+dy2[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 1:continue
                if dp[num+1][nx][ny] > cnt + 1:
                    dp[num+1][nx][ny] = cnt + 1
                    q.append((nx,ny,num+1,cnt+1))
print(ans)
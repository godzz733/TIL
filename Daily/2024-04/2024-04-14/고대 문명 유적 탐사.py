from copy import deepcopy
from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(5)]
lst = list(map(int,input().split()))[::-1]
dxy = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
turn_xy = [(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)]
def solve():
    def turn(x,y):
        global arr
        nonlocal num
        tem = deepcopy(arr)
        for k in range(4):
            q = [tem[x+dx][y+dy] for dx,dy in dxy]
            for i in range(8):
                nx,ny = x+turn_xy[i][0],y+turn_xy[i][1]
                tem[nx][ny] = q[i]
            v = [[0]*5 for _ in range(5)]
            tem_num = 0
            for i in range(5):
                for j in range(5):
                    if not v[i][j]:
                        tem_num += check_num(tem,v,i,j)
            if tem_num > num[0]:
                num = [tem_num,x,y,k+1]
            elif tem_num == num[0] and k+1 < num[3]:
                num = [tem_num,x,y,k+1]
    for _ in range(n):
        num = [0,0,0,0]
        for i in range(1,4):
            for j in range(1,4):
                turn(j,i)
        if num[0] == 0:
            break
        turn_cnt(num[1],num[2],num[3])
        
def check_num(arr, v, x,y):
    v[x][y] = 1
    cnt = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            nx,ny = x+dx,y+dy
            if 0<=nx<5 and 0<=ny<5 and not v[nx][ny] and arr[nx][ny] == arr[x][y]:
                v[nx][ny] = 1
                q.append((nx,ny))
                cnt += 1
    return cnt if cnt >= 3 else 0
    
def turn_cnt(x,y,cnt):
    global arr, lst
    num = 0
    c = 1
    for _ in range(cnt):
        q = [arr[x+dx][y+dy] for dx,dy in dxy]
        for i in range(8):
            nx,ny = x+turn_xy[i][0],y+turn_xy[i][1]
            arr[nx][ny] = q[i]
    while c:
        c = 0
        v = [[0]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if arr[i][j] and not v[i][j]:
                    num += real_del(i,j,v)
        for j in range(5):
            for i in range(4,-1,-1):
                if not arr[i][j] and lst:
                    arr[i][j] = lst.pop()
                    c = 1
    print(num, end=" ")
    
def real_del(x,y,v):
    global arr
    v[x][y] = 1
    cnt = 1
    q = deque()
    q.append((x,y))
    lst = [(x,y)]
    while q:
        x,y = q.popleft()
        for dx,dy in (-1,0),(1,0),(0,-1),(0,1):
            nx,ny = x+dx,y+dy
            if 0<=nx<5 and 0<=ny<5 and not v[nx][ny] and arr[nx][ny] == arr[x][y]:
                v[nx][ny] = 1
                q.append((nx,ny))
                lst.append((nx,ny))
                cnt += 1
    if cnt >= 3:
        for x,y in lst:
            arr[x][y] = 0
        return cnt
    return 0
solve()
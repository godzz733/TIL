n,m,k = map(int,input().split())
tem = [list(map(int,input().split())) for _ in range(n)]
home = [0,0]
arr = []
for i in range(n):
    for j in range(n):
        if tem[i][j] == 1:
            home = [i,j]
        elif tem[i][j] == 2:
            arr.append([i,j])
size = len(arr)
ans = 0
health = m
v = [0]*size 
def check(now,cnt, idx):
    global ans, health, v
    if ans > cnt + size - idx:
        return
    if idx == size:
        if abs(home[0]-now[0])+abs(home[1]-now[1]) <= health:
            ans = max(ans,cnt)
        return
    for i in range(size):
        x,y = arr[i]
        if v[i] == 0:
            if abs(now[0]-x)+abs(now[1]-y) <= health:
                v[i] = 1
                health -= abs(now[0]-x)+abs(now[1]-y)
                health += k
                check([x,y],cnt+1,idx+1)
                v[i] = 0
                health -= k
                health += abs(now[0]-x)+abs(now[1]-y)
            v[i] = 1
            check(now,cnt,idx+1)
            v[i] = 0
check(home,0,0)
print(ans)
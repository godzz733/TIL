import sys;I = sys.stdin.readline
from collections import defaultdict
n,m,l = map(int,I().rstrip().split())
arr = [list(I().rstrip()) for _ in range(n)]
s = I().rstrip()
dic = defaultdict(list)
for i in range(n):
    for j in range(m):
        dic[arr[i][j]].append((i,j))
x,y = 0,0
idx = 0
num = [0,0]
ans = []
tem = []
dx = [0,'R','L']
dy = [0,'D','U']
tx,ty = 0,0
while 1:
    try:
        nx,ny = dic[s[idx]].pop()
    except:
        break
    for i in range(abs(nx-x)):
        tem.append(dy[(nx-x)//abs(nx-x)])
    for i in range(abs(ny-y)):
        tem.append(dx[(ny-y)//abs(ny-y)])
    x,y = nx,ny
    tem.append('P')
    idx += 1
    if idx == len(s):
        num[0] += 1
        idx = 0
        ans.extend(tem)
        num[1] += len(tem)
        tem = []
        tx,ty = x,y
if num[0] == 0:
    x,y = 0, 0
    num = [0,0]
x,y = tx,ty
for i in range(n-x-1):
    ans.append('D')
for i in range(m-y-1):
    ans.append('R')
num[1] += n-x + m-y - 2
print(*num)
print(''.join(ans))
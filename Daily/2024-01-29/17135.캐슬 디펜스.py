n,m,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

ans = 0
enemy = set()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            enemy.add((i,j))

def find_ans(lst: set,bow: list):
    tans = 0
    for j in range(n):
        _set = set()
        del_set = set()
        for x,y in bow:
            distance = int(1e9)
            for x1,y1 in lst:
                if x1 == n-j-1:
                    del_set.add((x1,y1))
                if abs(x-x1)+abs(y-y1) < distance:
                    distance = abs(x-x1)+abs(y-y1)
                    add_xy = (x1,y1)
                elif abs(x-x1)+abs(y-y1) == distance:
                    if y1 < add_xy[1]:
                        add_xy = (x1,y1)
            if distance <= d:
                _set.add(tuple(add_xy))
        tans += len(_set)
        for i in _set:
            lst.remove(i)
        for i in del_set:
            if i in lst:
                lst.remove(i)
        for i in range(3):
            bow[i][0] -= 1
        if not lst:
            break
    return tans

for i in range(m-2):
    for j in range(i+1,m-1):
        for k in range(j+1,m):
            bow = [[n,i],[n,j],[n,k]]
            ans = max(ans,find_ans(enemy.copy(),bow))
print(ans)
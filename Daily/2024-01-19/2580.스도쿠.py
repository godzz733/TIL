import sys;input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(9)]
def find(x,y,num):
    for i in range(9):
        if arr[x][i] == num or arr[i][y] == num:
            return False
    for i in range(3*(x//3),3*(x//3)+3):
        for j in range(3*(y//3),3*(y//3)+3):
            if arr[i][j] == num:
                return False
    return True
def back(x,y):
    if x == 9:
        return True
    if y == 9:
        return back(x+1,0)
    if arr[x][y] == 0:
        for i in range(1,10):
            if find(x,y,i):
                arr[x][y] = i
                if back(x,y+1):
                    return True
                arr[x][y] = 0
        return False
    else:
        return back(x,y+1)
back(0,0)

for i in range(9):
    for j in range(9):
        print(arr[i][j],end=' ')
    print()
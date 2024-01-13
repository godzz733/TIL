import sys; I = sys.stdin.readline
n = int(I())
arr = [*map(int, I().split())]
m = int(I())
if arr[m] == -1:
    print(0)
    exit()
q = [m]
arr[m] = -2
while q:
    x = q.pop()
    for i in range(n):
        if arr[i] == x:
            q.append(i)
            arr[i] = -2
print(len([i for i in range(n) if arr[i] != -2 and i not in arr]))
import sys; input = sys.stdin.readline
n = int(input())
p = []
m = []
fun = 0
for _ in range(n):
    a,b = map(int,input().split())
    if b - a >= 0:
        p.append((a,b))
    else:
        m.append((a,b))
m.sort(key=lambda x: -x[1])
p.sort()
for a,b in p:
    if fun >= a:
        fun += b - a
    else:
        print(0)
        exit()
for a,b in m:
    if fun >= a:
        fun += b - a
    else:
        print(0)
        break
else:
    if fun >= 0:
        print(1)
    else:
        print(0)
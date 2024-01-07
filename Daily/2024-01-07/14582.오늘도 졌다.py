a,b = open(0)
ans = 0
for x,y in zip(map(int,a.split()),map(int,b.split())):
    ans += x
    if ans > 0:
        print('Yes')
        break
    ans -= y
else:
    print('No')
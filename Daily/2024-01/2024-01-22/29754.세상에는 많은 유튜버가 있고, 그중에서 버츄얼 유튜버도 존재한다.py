import sys;I = sys.stdin.readline
n,m = map(int,I().split())
ans = set()
tem = [[] for _ in range(m//7)]
for _ in range(n):
    a,b,c,d = map(str,I().split())
    ans.add(a)
    c1,c2 = c.split(':')
    d1,d2 = d.split(':')
    tem[(int(b)-1)//7].append([a,int(b),(int(d1)-int(c1)) * 60 + (int(d2)-int(c2))])
dic = {}
for j in tem:
    for i in j:
        a,b,c = i
        if a not in ans:
            continue
        if a not in dic:
            dic[a] = [c,1]
        else:
            dic[a][0] += c
            dic[a][1] += 1
    t = set([i for i in dic.keys()])
    ans &= t
    for x,y in dic.items():
        if y[0]//60 < 60 or y[1] < 5:
            try:
                ans.remove(x)
            except:
                pass
    dic = {}

for x in sorted(ans):
    print(x)
if len(ans) == 0:
    print(-1)
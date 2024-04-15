import sys; input = sys.stdin.readline
import heapq as h

command = int(input())
tem = list(map(int, input().split()))[1:]
n, m = tem[0], tem[1]
arr = [[] for _ in range(n+1)]
for i in range(2,m*3,3):
    a,b,c = tem[i],tem[i+1],tem[i+2]
    arr[a].append((b,c))
    arr[b].append((a,c))
def dik(start):
    d = [int(1e11)]*(n+1)
    d[start] = 0
    q = [(0,start)]
    while q:
        dist, now = h.heappop(q)
        if d[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < d[i[0]]:
                d[i[0]] = cost
                h.heappush(q, (cost, i[0]))
    return d
d = dik(0)
del_arr = set()
now = 0
_map = []
id = set()
for _ in range(command-1):
    com = list(map(int, input().split()))
    if com[0] == 200:
        if com[1] in del_arr:
            del_arr.remove(com[1])
        cost = -(com[2] - d[com[3]])
        h.heappush(_map,(cost if cost <= 0 else 100,com[1],com[3],com[2]))
    elif com[0] == 400:
        while _map:
            tem = h.heappop(_map)
            if tem[1] in del_arr:
                continue
            if -tem[0] < 0:
                print(-1)
                h.heappush(_map,tem)
                break
            else:
                print(tem[1])
                break
        else:
            print(-1)
    elif com[0] == 300:
        del_arr.add(com[1])
    else:
        d = dik(com[1])
        tem = []
        for i in range(len(_map)):
            a,b,c,e = _map[i]
            h.heappush(tem,(-(e-d[c]),b,c,e))
        _map = tem
from collections import deque
a,b,c = map(int,input().split())
ans = set([c])
v = set()
q = deque()
q.append((0,0,c))
v.add((0,0,c))
while q:
    x,y,z = q.popleft()
    t = [(min(z+x,a),y,max(0,z-a+x)),(x,min(z+y,b),max(0,z-b+y)),(min(y+x,a),max(0,y-a+x),z),
         (x,max(0,y-c+z),min(z+y,c)),(max(0,x-c+z),y,min(z+x,c)),(max(0,x-b+y),min(y+x,b),z)]
    for i in t:
        if i not in v:
            v.add(i)
            q.append(i)
            if not i[0]:
                ans.add(i[2])
print(*sorted(ans))
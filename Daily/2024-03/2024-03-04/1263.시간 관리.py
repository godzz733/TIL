import sys; input = sys.stdin.readline

n = int(input())

arr =[]

for i in range(n):

    a,b = map(int,input().split())

    arr.append((a,b))

arr.sort(key=lambda x:(x[1],x[0]))

st = 0

fi = 1000000

def check(time):

    for x,y in arr:

        if time + x > y:

            return False

        else:

            time += x

    return True

ans = -1

while st <= fi:

    mid = (st+fi) >> 1

    if check(mid):

        ans = max(ans,mid)

        st = mid + 1

    else:

        fi = mid-1

print(ans)
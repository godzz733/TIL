import sys; input = sys.stdin.readline
a,b = map(int, input().split())
c,d = map(int, input().split())
k = int(input())
t = 0
try:
    if b % k == 0:
        t = b // k
    else:
        t = b // k + 1
except:
    pass

def check(n):
    if b - n*k <= 0:
        return b*t - (t-1)*t//2 * k
    return n * b - (n-1)*n//2 * k
cnt = 0
st = 0; fi = 10**12
while st <= fi:
    mid = (st+fi)//2
    if check(mid) >= a:
        fi = mid - 1
        cnt = mid
    else:
        st = mid + 1
if not cnt:
    print(-1)
else:
    if d*cnt >= a + c:
        print(-1)
    else:
        print(cnt)
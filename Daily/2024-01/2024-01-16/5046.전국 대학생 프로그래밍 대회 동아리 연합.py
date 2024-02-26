import sys; I = sys.stdin.readline
n,b,h,w= map(int,I().split())
ans = int(1e9)
for _ in range(h):
    p = int(I())
    arr = list(map(int,I().split()))
    for i in arr:
        if i >= n and p*n <= b:
            ans = min(ans,p*n)
print(ans if ans != int(1e9) else 'stay home')
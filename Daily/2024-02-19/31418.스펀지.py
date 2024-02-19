import sys; input = sys.stdin.readline
n,m,k,t = map(int, input().split())
ans = 1
mod = 998244353
if t>=n and t>=m:
    for i in range(k):
        ans *= (n *m)
        ans %= mod
    print(ans%mod)
for _ in range(k):
    a,b = map(int, input().split())
    _a = a-t if a-t>=1 else 1
    _b = b-t if b-t>=1 else 1
    __a = a+t if a+t<=n else n
    __b = b+t if b+t<=m else m
    ans *= ((__a-_a+1)*(__b-_b+1))
    ans %= mod
print(ans%mod)
n,m = map(int, input().split())
n -= 1
ans = 0
arr = []
while n:
    tem = 1
    while tem <= n:
        tem <<= 1
    tem >>= 1
    n -= tem
    arr.append(tem)
arr2 = []
while m:
    tem = 1
    while tem <= m:
        tem <<= 1
    tem >>= 1
    m -= tem
    arr2.append(tem)
def ans(n):
    tem = 1
    re = n
    while tem <= n:
        tem <<= 1
        re += (n // tem) * (tem // 2)
    return re
print(sum([ans(i) for i in arr2]) - sum([ans(i) for i in arr]))
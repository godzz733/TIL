import sys; input = sys.stdin.readline
n, m = map(int, input().split())
arr = [set(list(input().rstrip())) for _ in range(n)]
for i in range(n):
    tem = 0
    for j in arr[i]:
        tem |= 1 << (ord(j) - 97)
    arr[i] = tem
num = 0
for _ in range(m):
    tem = 0
    a,b = map(str, input().split())
    if a == '1':
        num |= 1 << (ord(b) - 97)
    else:
        num &= ~(1 << (ord(b) - 97))
    for i in arr:
        if not i & num: tem += 1
    print(tem)
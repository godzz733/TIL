import sys
input = sys.stdin.readline
def check_num(x):
    global key
    for i in range(1<<x):
        t = bin(i)[2:].zfill(x)
        for j in range(1,x-1):
            if t[j] == '1' and (t[j-1] == '1' or t[j+1] == '1'):
                break
        else:
            key.add(i)
def check_cnt(x,y):
    for i in range(m):
        if x & (1<<i):
            if i > 0 and ((1 << (i-1)) & y): return 0
            if i < m-1 and ((1 << (i+1)) & y): return 0
    return 1


for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = [list(input()) for _ in range(n)]
    check = []
    for i in range(n):
        tem = 0
        for j in range(m):
            if arr[i][j] == 'x':
                tem |= 1<<j
        check.append(tem)
    dp = [[0 for i in range(1<<m)] for _ in range(n)]
    key = set()
    check_num(m)
    for i in key:
        if i & check[0]: continue
        dp[0][i] = bin(i).count('1')
    for i in range(1,n):
        for j in key:
            if j & check[i]: continue
            for k in key:
                if check_cnt(j,k):
                    dp[i][j] = max(dp[i][j],dp[i-1][k]+bin(j).count('1'))
    ans = 0
    for i in range(n):
        ans = max(ans,max(dp[i]))
    print(ans)
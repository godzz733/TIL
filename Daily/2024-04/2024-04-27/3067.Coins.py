import sys; input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [1] + [0] * (10000)
    m = int(input())
    for i in arr:
        for j in range(m+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
    print(dp[m])
import sys; input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
arr = list(map(int, input().split()))
for i in range(1,n+1):
    for j in range(i,n+1):
        dp[j] = max(dp[j], dp[j-i] + arr[i-1])
print(dp[n])
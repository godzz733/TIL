import sys; input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
dp = [0 for _ in range(n+1)]
for i in range(n):
    dp[arr[i]] = max(dp[arr[i]-1] + 1, dp[arr[i]])
print(n-max(dp))
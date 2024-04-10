import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = (m - arr[i])
if sum(arr) > m:
    print(0)
    exit()
mod = int(1e9) + 7
nums = [1]
for i in range(1,m+1):
    nums.append(nums[-1] * i % mod)
ans = nums[m]
tem = 1
for i in arr:
    tem *= nums[i]
    tem %= mod
tem *= nums[m - sum(arr)]
tem %= mod
print(ans * pow(tem, -1, mod) % mod)
import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [0]
for i in range(1,n):
    ans.append(ans[-1] + arr[i])
num = 0
for i in range(1,n):
    num = max(num, ans[n-1] - ans[i] + ans[n-1] - arr[i])
num2 = 0
arr = arr[::-1]
ans = [0]
for i in range(1,n):
    ans.append(ans[-1] + arr[i])

for i in range(1,n):
    num2 = max(num2, ans[n-1] - ans[i] + ans[n-1] - arr[i])

ans = [arr[0]]
for i in range(1,n):
    ans.append(ans[-1] + arr[i])
num3 = 0
for i in range(1,n-1):
    num3 = max(num3, ans[i] - ans[0] + ans[n-1] - ans[i-1] - arr[n-1])
print(max(num,num2,num3))
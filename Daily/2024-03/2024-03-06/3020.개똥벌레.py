import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
ans = [0] * (m+1)
for i in range(0,n,2):
    ans[0] += 1
    ans[arr[i]+1] -= 1
for i in range(m):
    ans[i+1] += ans[i]
ans2 = [0] * (m+1)
for i in range(1,n,2):
    ans2[m] += 1
    ans2[m-arr[i]-1] -= 1
for i in range(m,0,-1):
    ans2[i-1] += ans2[i]
real_ans = [0] * m
for i in range(1,m+1):
    real_ans[i-1] += ans[i]
for i in range(m):
    real_ans[i] += ans2[i]
_min = min(real_ans)
print(_min, real_ans.count(_min))
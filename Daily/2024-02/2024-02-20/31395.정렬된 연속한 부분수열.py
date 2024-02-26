import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = 0
tem = arr[0]
cnt = 1
for i in arr[1:]:
    if tem < i:
        tem = i
        cnt += 1
    else:
        ans += cnt*(cnt+1)//2
        tem = i
        cnt = 1
ans += cnt*(cnt+1)//2
print(ans)
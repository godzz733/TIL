import sys; input = sys.stdin.readline
n = int(input())
arr = [*map(int,input().split())]
arr2 = [*map(int,input().split())]
a = [0] * (int(1e6)+1)
for i in range(n):
    a[arr[i]] += 1
    a[arr2[i]] -= 1
ans = 0
for i in a:
    ans += abs(i)
print(ans//2)
import sys;input = sys.stdin.readline
n,m = map(int, input().split())
d = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if max(abs(i-n)+abs(j-m),i+j-2,i+abs(j-m)-1, abs(i-n)+j-1) < d:
            ans += 1
print(ans)
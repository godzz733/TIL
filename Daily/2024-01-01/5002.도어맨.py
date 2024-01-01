import sys;input = sys.stdin.readline
n = int(input())
a,b = 0,0
ans = 0
key = 0
for i in input().rstrip():
    if i == 'M':
        a += 1
    else: b += 1
    if abs(a-b) > n:
        if not key:
            key = 1
        else:
            break
    else:
        key = 0
    ans += 1
print(ans-key)
import sys;input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
arr = deque([*map(int, input().split())])
ans = 0
time = 0
while arr:
    if not time:
        time = arr.popleft() + m
        ans += 1
    while arr and arr[0] <= time:
        arr.popleft()
        if not arr:
            print(ans)
            exit()
    time = 0
print(ans)
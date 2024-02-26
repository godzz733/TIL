import sys; I = sys.stdin.readline
from itertools import permutations
import bisect
arr = []
for j in range(1, 10):
    for i in permutations(range(1, 10), j):
        arr.append(int(''.join(map(str, i))))
while 1:
    try:
        n = int(I())
        idx = bisect.bisect_right(arr, n)
        print(arr[idx]) if idx < 986409 else print(0)
    except:
        break
        
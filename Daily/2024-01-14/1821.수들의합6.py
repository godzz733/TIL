import sys; input = sys.stdin.readline
from itertools import permutations
n,m = map(int,input().split())
arr = [i for i in range(1,n+1)]
def check(arr):
    t = arr[0] + arr[-1]
    for i in arr[1:len(arr)-1]:
        t += (n-1)*i
    if t == m:
        return True
    return False
if n == 1:
    print(1)
    exit()
for i in permutations(arr,n):
    if check(list(i)):
        print(*i)
        break
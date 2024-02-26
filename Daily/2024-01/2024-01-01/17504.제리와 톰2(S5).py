import sys;input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]
a,b = 1,arr[-1]
for i in arr[:-1][::-1]:
    a += b*i
    a,b = b,a
print(b-a,b)
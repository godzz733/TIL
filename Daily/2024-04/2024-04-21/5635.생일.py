import sys; input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a,b,c,d = map(str, input().split())
    arr.append((int(d),int(c),int(b),a))
arr.sort(reverse=True)

print(arr[0][3])
print(arr[-1][3])
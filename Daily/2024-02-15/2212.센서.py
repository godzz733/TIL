import sys; input = sys.stdin.readline
n = int(input())
k = int(input())
tarr = list(set([*map(int, input().split())]))
tarr.sort()
arr = sorted([tarr[i+1] - tarr[i] for i in range(len(tarr)-1)])
print(sum(arr[:len(arr)-k+1]) if len(arr)-k+1 > 0 else 0)
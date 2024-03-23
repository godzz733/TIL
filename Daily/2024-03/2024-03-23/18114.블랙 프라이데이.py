import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
if m in arr:
    print(1)
    exit()
dic = {i:0 for i in arr}
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i] + arr[j] == m:
            print(1)
            exit()
        if m - arr[i] - arr[j] in dic and m - arr[i] - arr[j] not in (arr[i],arr[j]):
            print(1)
            exit()
print(0)
n = int(input())
arr = set([int(input()) for _ in range(n)])
ans = 0
for i in arr:
    tem = 0
    for j in range(i,i+5):
        if j in arr:
            tem += 1
    ans = max(ans,tem)
print(max(5-ans,0))
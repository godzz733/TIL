n,m = map(int,input().split())
arr = [0] * 40 + list(map(int,bin(n)[2:]))
ans = [0] * (len(arr))
t = bin(m)[2:]
idx = len(t)-1
for i in range(len(arr)-1,-1,-1):
    if arr[i] == 0:
        ans[i] = t[idx]
        idx -= 1
    if idx == -1:
        break
print(int(''.join(list(map(str,ans))),2))
idx = 0
ans = 0
n = int(input())
arr = input()
for i in range(n):
    if arr[i] == 'O':
        ans += idx + i + 1
        idx += 1
    else:
        idx = 0
print(ans)
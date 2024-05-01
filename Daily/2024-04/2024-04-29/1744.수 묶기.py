import sys; input = sys.stdin.readline
arr = [[],[],[]]
n = int(input())
for _ in range(n):
    x = int(input())
    if x < 0: arr[0].append(x)
    elif x == 0: arr[1].append(x)
    else: arr[2].append(x)

arr[0].sort()
arr[2].sort()
ans = 0
for i in range(0,len(arr[0]),2):
    if i+1 >= len(arr[0]): continue
    ans += arr[0][i]*arr[0][i+1]
for i in range(len(arr[2])-1,-1,-2):
    if i-1 < 0: continue
    ans += max(arr[2][i]*arr[2][i-1], arr[2][i] + arr[2][i-1])
a,b,c = len(arr[0]) & 1, len(arr[1]), len(arr[2]) & 1
if a and b and c: ans += arr[2][0]
elif a and b and not c:pass
elif a and not b and c: ans += max(arr[0][-1] * arr[2][0], arr[0][-1] + arr[2][0])
elif a and not b and not c: ans += arr[0][-1]
elif not a and b and c: ans += arr[2][0]
elif not a and b and not c: pass
elif not a and not b and c: ans += arr[2][0]
elif not a and not b and not c: pass

print(ans)

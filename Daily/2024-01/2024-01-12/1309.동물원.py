n = open(0).readline()
ans = [3,2,1]
for i in range(n-1):
    ans[1] += ans[2] << 1
    ans[2] = ans[0]
    ans[0] = ans[1] + ans[2]
    for j in range(3):
        ans[j] %= 9901
print(ans[0])
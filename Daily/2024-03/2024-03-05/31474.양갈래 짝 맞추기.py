n = int(input())
ans = 1
for i in range(1+(n>>1),n+1):
    ans *= i
ans //= 2**(n>>1)
print(ans)
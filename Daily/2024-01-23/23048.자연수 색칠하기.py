n = int(input())
primes = [0] * (n+1)
ans = 1
primes[1] = 1
for i in range(2,n+1):
    if not primes[i]:
        ans += 1
        for j in range(i,n+1,i):
            primes[j] = ans
print(ans)
print(*primes[1:])
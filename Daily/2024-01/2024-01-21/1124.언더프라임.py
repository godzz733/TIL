import sys; I = sys.stdin.readline
prime = [False, False] + [True] * 100000
primes = []
arr = [0] * 100001
for i in range(2,50001):
    if prime[i]:
        primes.append(i)
        for j in range(i*2,100001,i):
            prime[j] = False
            tem = j
            while tem % i == 0:
                tem //= i
                arr[j] += 1
n,m = map(int,I().split())
ans = 0
for i in range(n,m+1):
    if prime[arr[i]]:
        ans += 1
print(ans)
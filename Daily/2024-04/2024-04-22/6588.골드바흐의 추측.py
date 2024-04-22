import sys; input = sys.stdin.readline
prime = [False] * (1000001)
primes = [False] * 1000001
primess = []
for i in range(2, 1000001):
    if prime[i]: continue
    primes[i] = True
    primess.append(i)
    for j in range(i+i, 1000001, i):
        prime[j] = True


while 1:
    x = int(input())
    if not x: break
    for i in primess:
        if primes[x - i]:
            print("{} = {} + {}".format(x, i, x - i))
            break